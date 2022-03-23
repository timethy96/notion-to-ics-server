# notion-to-ics-server

This is a self-hosted on-demand ics serving converter api for notion calendars. It was written quickly and dirty for the only purpose of my own use. I have no time to give support or to update the code. Feel free to take the code and make something of your own. I am not responsible for anything that happens!

## Docker environment variables:

| Env var | Description | Default |
| ------------- | ------------- | ------------- |
| SECRET_PW | Password for ICS-Converting request used later in URL. | `changeThisToAnyPassword` |
| NOTION_TOKEN | Your Notion token v2 (See [mianfg/notion-to-ics](https://github.com/mianfg/notion-to-ics) for further description.) | `Notion_token_v2_cookie` |

## Request URL

The request URL consists of some variables and options:
`https://yourDomain.com/?password={SECRET_PW}&calendar_url={calendar_url}&categories_property={categories_property}&show_others={show_others}`

| var | Description | Type |
| ------------- | ------------- | ------------- |
| SECRET_PW | Password for ICS-Converting set in env-vars. | String |
| calendar_url | full Notion calendar URL | String |
| categroies_property | Main Calendar Property (default: tag) | String |
| show_others | Show other calendar properties in description (default: true) | Boolean |



## Credits
It is based on [mianfg/notion-to-ics](https://github.com/mianfg/notion-to-ics)
and [tiangolo/fastapi](https://github.com/tiangolo/fastapi)