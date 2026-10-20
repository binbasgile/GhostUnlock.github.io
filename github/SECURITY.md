# Security Protocols for GhostUnlock SaaS

## 1. Payload Regeneration & Evasion (FRP)
- **Dynamic Hashing:** Every time a bypass payload is loaded, it includes a random salt (`uuid.uuid4()`) to ensure `md5sum` of the file changes slightly on every run, evading strict IP-based signature blocking by Google servers.
- **IP Rotation Strategy:** If an error code like `HTTP 403 Too Many Requests` or `Pattern_Required` occurs 2 times, the system immediately pulls a new proxy from the pool before retrying.
- **Session TTL:** Each unlock session (ADB connection) has a Time-To-Live (TTL). After 1 hour of inactivity, the worker forces a re-authentication via a secondary secure channel.

## 2. iCloud Token Security
- **Server-Side Tokens:** The `IcloudRemover` generates cryptographically random UUIDs (`str(uuid.uuid4())`) for activation tokens. These are stored encrypted in SQL using AES-256 if `CONFIG['encryption'] == True`.
- **Token Expiration:** If an iCloud token fails validation more than 3 times, it is invalidated from the DB to prevent "stale key" attacks against the Apple Activation Server.

## 3. Remote Command Isolation (IMEI)
- When executing remote commands (Track/Reset/Lock), the system creates a dedicated socket connection per IMEI. Commands are serialized with HMAC-SHA256 signatures to ensure they haven't been tampered with mid-transit.
