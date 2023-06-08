
# Phone Object

## Structure

`PhoneObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone` | `string` | Optional | Automatically populated with the wa_id value as a formatted phone number. |
| `wa_id` | `string` | Optional | WhatsApp ID. |
| `mtype` | [`PhoneTypeEnum`](../../doc/models/phone-type-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "phone": "<CONTACT_PHONE>",
  "wa_id": "<CONTACT_WA_ID>",
  "type": "HOME"
}
```

