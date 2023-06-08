
# Retrieve Media URL Response

## Structure

`RetrieveMediaURLResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `messaging_product` | `string` | Required | - |
| `url` | `string` | Required | - |
| `mime_type` | `string` | Required | - |
| `sha_256` | `string` | Required | - |
| `file_size` | `string` | Required | - |
| `id` | `string` | Required | - |

## Example (as JSON)

```json
{
  "messaging_product": "whatsapp",
  "url": "<URL>",
  "mime_type": "image/jpeg",
  "sha256": "<HASH>",
  "file_size": "303833",
  "id": "2621233374848975"
}
```

