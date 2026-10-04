using Microsoft.Extensions.Options;
using System.Security.Cryptography;

namespace Services.Application.HashPassword
{
    public class PasswordHasher : IPasswordHasher
    {
        private const int SaltSize = 16; // 128 bit 
        private const int KeySize = 32; // 256 bit

        public PasswordHasher(IOptions<HashingOptions> options)
        {
            Options = options.Value;
        }

        private HashingOptions Options { get; }

        public string Hash(string password)
        {
            var salt = RandomNumberGenerator.GetBytes(SaltSize);
            var key = Rfc2898DeriveBytes.Pbkdf2(password, salt, Options.Iterations, HashAlgorithmName.SHA256, KeySize);

            return $"{Options.Iterations}.{Convert.ToBase64String(salt)}.{Convert.ToBase64String(key)}";
        }

        public (bool Verified, bool NeedsUpgrade) Check(string hash, string password)
        {
            if (string.IsNullOrWhiteSpace(hash))
            {
                return (false, false);
            }

            var parts = hash.Split('.', 3);

            if (parts.Length != 3)
            {
                return (false, false);
            }

            var iterations = Convert.ToInt32(parts[0]);
            var salt = Convert.FromBase64String(parts[1]);
            var key = Convert.FromBase64String(parts[2]);

            var needsUpgrade = iterations != Options.Iterations;

            var keyToCheck = Rfc2898DeriveBytes.Pbkdf2(password, salt, iterations, HashAlgorithmName.SHA256, KeySize);

            var verified = CryptographicOperations.FixedTimeEquals(keyToCheck, key);

            return (verified, needsUpgrade);
        }
    }
}
