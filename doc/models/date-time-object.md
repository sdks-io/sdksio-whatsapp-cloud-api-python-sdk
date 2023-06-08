
# Date Time Object

## Structure

`DateTimeObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fallback_value` | `string` | Required | Default text. For Cloud API, we always use the fallback value, and we do not attempt to localize using other optional fields. |
| `day_of_week` | `int` | Optional | - |
| `year` | `int` | Optional | - |
| `month` | `int` | Optional | - |
| `day_of_month` | `int` | Optional | - |
| `hour` | `int` | Optional | - |
| `minute` | `int` | Optional | - |
| `calendar` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "fallback_value": "February 25, 1977",
  "day_of_week": 5,
  "year": 1977,
  "month": 2,
  "day_of_month": 25,
  "hour": 15,
  "minute": 33,
  "calendar": "GREGORIAN"
}
```

