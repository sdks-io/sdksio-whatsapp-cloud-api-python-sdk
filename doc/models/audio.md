
# Audio

## Structure

`Audio`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The media object ID. Required when you are not using a link. |
| `link` | `string` | Optional | The protocol and URL of the media to be sent. Use only with HTTP/HTTPS URLs. Required when you are not using an uploaded media ID. |

## Example (as JSON)

```json
{
  "id": "<media-object-id>",
  "link": "link0"
}
```

