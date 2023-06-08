# Business Profiles

```python
business_profiles_controller = client.business_profiles
```

## Class Name

`BusinessProfilesController`

## Methods

* [Get Business Profile ID](../../doc/controllers/business-profiles.md#get-business-profile-id)
* [Update Business Profile](../../doc/controllers/business-profiles.md#update-business-profile)


# Get Business Profile ID

Use this endpoint to retrieve your business’ profile. This business profile is visible to consumers in the chat thread next to the profile photo. The profile information will contain a business profile ID which you can use to make API calls.

```python
def get_business_profile_id(self,
                           phone_number_id,
                           fields=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_number_id` | `string` | Template, Required | - |
| `fields` | `string` | Query, Optional | Here you can specify what you want to know from your business as a comma separated list of fields. Available fields include: id, about, messaging_product, address, description, vertical, email, websites, profile_picture_url |

## Response Type

[`GetBusinessProfileIDResponse`](../../doc/models/get-business-profile-id-response.md)

## Example Usage

```python
phone_number_id = 'Phone-Number-ID6'

fields = 'about,address,description,email,profile_picture_url,websites,vertical'

result = business_profiles_controller.get_business_profile_id(
    phone_number_id,
    fields
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "messaging_product": "whatsapp",
      "address": "ADDRESS",
      "description": "DESCRIPTION",
      "vertical": "UNDEFINED",
      "email": "EMAIL",
      "websites": [
        "https://WEBSITE-1",
        "https://WEBSITE-2"
      ],
      "profile_picture_url": "https://URL",
      "id": "BUSINESS_PROFILE_ID"
    }
  ]
}
```


# Update Business Profile

Use this endpoint to update your business’ profile information such as the business description, email or address.

```python
def update_business_profile(self,
                           phone_number_id,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `phone_number_id` | `string` | Template, Required | - |
| `body` | [`UpdateBusinessProfileRequest`](../../doc/models/update-business-profile-request.md) | Body, Required | - |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
phone_number_id = 'Phone-Number-ID6'

body = UpdateBusinessProfileRequest(
    messaging_product='whatsapp',
    address='ADDRESS',
    description='DESCRIPTION',
    vertical=VerticalEnum.UNDEFINED,
    email='EMAIL',
    websites=[
        'https://WEBSITE-1',
        'https://WEBSITE-2'
    ],
    profile_picture_url='https://URL'
)

result = business_profiles_controller.update_business_profile(
    phone_number_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

