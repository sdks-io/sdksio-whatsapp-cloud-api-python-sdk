
# Image

## Structure

`Image`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The media object ID. Required when you are not using a link. |
| `link` | `string` | Optional | The protocol and URL of the media to be sent. Use only with HTTP/HTTPS URLs. Required when you are not using an uploaded media ID. |
| `caption` | `string` | Optional | Describes the specified image media. |

## Example (as JSON)

```json
{
  "id": "<image-object-id>",
  "link": "link0",
  "caption": "caption4"
}
```

