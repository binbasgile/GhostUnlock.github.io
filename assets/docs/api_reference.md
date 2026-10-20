# GhostUnlock API Reference v1

## Base URL: `/api/v1/`

### Unlock Device Endpoint (`POST /unlock`)

#### Request Body Schema (`application/json`)
| Field | Type   | Required | Description                                |
|-------|--------|----------|---------------------------------------------|
| device\_type | string | Yes      | `"android"`, `"iphone"`, or `"simlock"`     |
| imei    | string | No       | IMEI for tracking later, optional on first try (optional param) |
| method  | string | No       | Override default algorithm version          |

#### Response Example (Success - 200 OK)
```json
{
  "message": "Android process initiated.", 
  "job_id": 1098, 
  "type": "frp_bypass",
  "status_code": 200,
  "time_taken_ms": 450.123 // Optional timestamp diff
}
