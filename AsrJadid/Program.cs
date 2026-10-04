using AccountManagment.Infrastructure.Configuration;
using AsrJadid.Data;
using Microsoft.AspNetCore.Authentication.Cookies;
using Services.Application;
using Services.Application.AuthHelper;
using Services.Application.HashPassword;
using Services.Model;
using Services.Models;
using StoneManagement.Infrastructure.Configuration;

// قالب‌بندی اعداد به‌صورت قطعی (ارقام لاتین در کد و ارقام فارسی از طریق Tools)
System.Globalization.CultureInfo.DefaultThreadCurrentCulture = System.Globalization.CultureInfo.InvariantCulture;
System.Globalization.CultureInfo.DefaultThreadCurrentUICulture = System.Globalization.CultureInfo.InvariantCulture;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddHttpContextAccessor();

var connectionString = builder.Configuration.GetConnectionString("AsrjadidDB")
    ?? "Server=.;Database=AsrJadidDB;Integrated Security=True;TrustServerCertificate=True;";

SMInfrastructureConfigurationBootStraper.Configure(builder.Services, connectionString);
AMInfrastructureConfigurationBootStraper.Configure(builder.Services, connectionString);

// سرویس‌های مشترک
builder.Services.Configure<HashingOptions>(builder.Configuration.GetSection("Hashing"));
builder.Services.AddScoped<IPasswordHasher, PasswordHasher>();
builder.Services.AddScoped<IAuthHelper, AuthHelper>();
builder.Services.AddTransient<IFileUploader, FileUploader>();

// احراز هویت کوکی‌محور
builder.Services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
    .AddCookie(options =>
    {
        options.LoginPath = "/Login";
        options.LogoutPath = "/Logout";
        options.AccessDeniedPath = "/Login";
        options.ExpireTimeSpan = TimeSpan.FromDays(30);
        options.SlidingExpiration = true;
        options.Cookie.IsEssential = true;
        options.Cookie.Name = "AsrJadid.Auth";
    });

builder.Services.AddAuthorization();

builder.Services.Configure<CookiePolicyOptions>(options =>
{
    options.CheckConsentNeeded = context => false;
    options.MinimumSameSitePolicy = SameSiteMode.Lax;
});

// Add services to the container.
builder.Services.AddRazorPages(options =>
{
    // پنل مدیریت فقط برای نقش مدیر
    options.Conventions.AuthorizeFolder("/Admin", RolesCode.Admin);
    options.Conventions.AllowAnonymousToPage("/Admin/Login");

    // صفحات کاربری نیاز به ورود دارند
    options.Conventions.AuthorizePage("/Dashboard");
    options.Conventions.AuthorizePage("/Profile");
    options.Conventions.AuthorizePage("/Orders");
    options.Conventions.AuthorizePage("/Order");
});

var app = builder.Build();

// ساخت پایگاه داده و داده‌های اولیه در اولین اجرا
using (var scope = app.Services.CreateScope())
{
    SeedData.Initialize(scope.ServiceProvider);
}

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

// صفحه خطای اختصاصی برای کدهای وضعیت (۴۰۴، ۴۰۳ و …) با همان قالب سایت
app.UseStatusCodePagesWithReExecute("/Error", "?code={0}");

app.UseHttpsRedirection();

app.UseRouting();

app.UseCookiePolicy();

app.UseAuthentication();
app.UseAuthorization();

// فایل‌های استاتیک زمان اجرا (تصاویر آپلودشده در wwwroot/Pictures) توسط MapStaticAssets
// پوشش داده نمی‌شوند؛ بنابراین UseStaticFiles نیز فعال است.
app.UseStaticFiles();

app.MapStaticAssets();
app.MapRazorPages()
   .WithStaticAssets();

app.Run();
