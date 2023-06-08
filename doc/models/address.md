
# Address

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `string` | Optional | Street number and name |
| `city` | `string` | Optional | City name. |
| `state` | `string` | Optional | State abbreviation. |
| `zip` | `string` | Optional | ZIP code. |
| `country` | `string` | Optional | Full country name. |
| `country_code` | `string` | Optional | Two-letter country abbreviation. |
| `mtype` | [`PersonalInformationTypeEnum`](../../doc/models/personal-information-type-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "street": "<ADDRESS_STREET>",
  "city": "<ADDRESS_CITY>",
  "state": "<ADDRESS_STATE>",
  "zip": "<ADDRESS_ZIP>",
  "country": "<ADDRESS_COUNTRY>",
  "country_code": "<ADDRESS_COUNTRY_CODE>",
  "type": "HOME"
}
```

