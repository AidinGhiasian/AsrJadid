using Microsoft.AspNetCore.Identity;
using Microsoft.Extensions.Configuration.UserSecrets;
using Services.Application;
using Services.Application.HashPassword;
using Services.Model;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddHttpContextAccessor();

//var contectionstring = builder.Configuration.GetConnectionString("AsrjadidDB");
//StoneMInfrastructureConfigurationBootstraper.Configure(builder.Services, contectionstring);
//AccountMInfrastructureConfigurationBootstraper.Configure(builder.Services, contectionstring);

builder.Services.AddScoped<IPasswordHasher, PasswordHasher>();
builder.Services.AddTransient<IFileUploader, FileUploader>();

builder.Services.Configure<CookiePolicyOptions>(options =>
{
    options.CheckConsentNeeded = context => true;
    options.MinimumSameSitePolicy = SameSiteMode.Lax;
});


// Add services to the container.
builder.Services.AddRazorPages();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseRouting();

app.UseAuthorization();

app.MapStaticAssets();
app.MapRazorPages()
   .WithStaticAssets();

app.Run();
