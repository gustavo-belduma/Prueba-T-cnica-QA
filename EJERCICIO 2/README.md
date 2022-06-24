## Inicio
1. Registrarse en el [sitio web](https://auth.blazemeter.com/auth/realms/blazect/protocol/saml/clients/blazemeter)
2. [Generate a new API key](https://guide.blazemeter.com/hc/en-us/articles/115002213289-BlazeMeter-API-keys-#apikey2)
3. Pruebas de conexión 
   1. Terminal
   ```
   curl 'https://a.blazemeter.com/api/v4/user' --user 'api_key_id:api_key_secret'
   ```
   2. Herramienta Postman
   ![Autenticación básica](img/exercise_2_1.png?raw=true "Title")
    
## Entornos de variable
![Entornos de variable](img/exercise_2_5.png?raw=true "Title")


## Desarrollo del ejercicio

Tomando como referencia la [página oficial](https://api.blazemeter.com/functional)


### Crear un [nuevo usuario](https://api.blazemeter.com/functional/#add-user-to-account)
Entradas:
```
{
    "invitations": [
        {
            "inviteeEmail": "myName@myDomain.com",
            "attachAutomatically": true,
            "accountRoles": [
                "standard"
            ],
            "workspacesId": [
                1250586
            ],
            "workspacesRoles": [
                "tester"
            ]
        }
    ]
}
```

Resultado y/o Salida:
![creación nuevo usuario](img/exercise_2_2.png?raw=true "Title")

Listando Cuentas de usuario
![creación nuevo usuario](img/exercise_2_4.png?raw=true "Title")
```
{
    "api_version": 4,
    "error": null,
    "result": [
        {
            "id": "62b5cd0f73f40e2c9e1ff7b3",
            "inviteeEmail": "myname@mydomain.com",
            "token": "eYfyxUJjXoG8",
            "accountRoles": [
                "standard"
            ],
            "workspacesRoles": [
                "tester"
            ],
            "attachAutomatically": true,
            "created": 1656081679,
            "updated": 1656081679,
            "accountId": 1218124,
            "inviteeUserId": 1358531,
            "invitedById": 1698793,
            "workspacesId": [
                1250586
            ],
            "accountName": "Default Account",
            "acceptUrl": "https://a.blazemeter.com/api/v4/accounts/1218124/invitations/62b5cd0f73f40e2c9e1ff7b3/accept/eYfyxUJjXoG8",
            "rejectUrl": "https://a.blazemeter.com/api/v4/accounts/1218124/invitations/62b5cd0f73f40e2c9e1ff7b3/reject/eYfyxUJjXoG8",
            "invitingEmail": "gustavo.belduma@gmail.com",
            "invitingName": "Gustavo Belduma",
            "workspaceNames": [
                "Default workspace"
            ]
        }
    ],
    "request_id": "62b5cd0ded25c"
}
```

### Intentar crear un usuario ya existente
![creación usuario ya existente](img/exercise_2_3.png?raw=true "Title")
Entrada:
```
{
    "invitations": [
        {
            "inviteeEmail": "myName@myDomain.com",
            "attachAutomatically": true,
            "accountRoles": [
                "standard"
            ],
            "workspacesId": [
                1250586
            ],
            "workspacesRoles": [
                "tester"
            ]
        }
    ]
}
```
Salida:
```
{
    "error": {
        "code": 400,
        "message": "Bad Request: User is already a member on this account"
    },
    "api_version": 4,
    "result": null,
    "request_id": "62b5cecb25e63"
}
```

### Usuario y password correcto en login ([Autenticación Básica](https://api.blazemeter.com/functional/#authorization-using-basic-authentication))
Entradas:
```
curl --location --request GET 'https://a.blazemeter.com/api/v4/user' \
--header 'Authorization: Basic MTA4MTY5Mjc5ZmM2NzgyMDYxNjBhMGNjOmY1MmYzYmVjOWFhNGE5ZmVjYmI2ZTU2ZjQ4MjYyYjRlMjIzZTU4NjFlYjNjYmVlMDAyZjRjZjEyZjEyYzRkNmI0MTc0MzY1ZA==' \
--header 'Cookie: bzm_sess=3161f8cb2c07ec81e5459ccc1bb99d6a'
```

Salidas:
```
{
    "api_version": 4,
    "error": null,
    "result": {
        "id": 1698793,
        "email": "gustavo.belduma@gmail.com",
        "passwordUpdateTime": 1656078061,
        "access": 1656082950,
        "login": 1656078072,
        "firstName": "Gustavo",
        "lastName": "Belduma",
        "timezone": 0,
        "enabled": true,
        "roles": [
            "user",
            "new-billing",
            "authenticated"
        ],
        "keycloakGoogleRegister": false,
        "apiTestingVersion": 0,
        "created": 1656078061,
        "updated": 1656078062,
        "elev_io_user_hash": "6a9995d3fe8db6e140797d6f637024f93f7e88dbe7d50ce22c6b809aceda5e2a",
        "defaultProject": {
            "accountId": 1218124,
            "accountName": "Default Account",
            "workspaceName": "Default workspace",
            "id": 1498907,
            "name": "Default project",
            "userId": null,
            "description": null,
            "underMigration": null,
            "created": 1656078062,
            "updated": 1656078062,
            "organizationId": null,
            "workspaceId": 1250586
        },
        "defaultProjectId": 1498907,
        "displayName": "Gustavo Belduma",
        "features": [],
        "mail": "gustavo.belduma@gmail.com",
        "name": "Gustavo",
        "preferences": {
            "id": "62b5beef4c4f1e790569f455",
            "userId": 1698793,
            "activePlatform": "functional",
            "visitedMockServices": true,
            "activeProjectId": 1498907,
            "activeOrganizationId": 1250586,
            "activeWorkspaceId": 1250586,
            "activeAccountId": 1218124,
            "aggregateReportFields": [
                "labelName",
                "samples",
                "avgResponseTime",
                "90line",
                "95line",
                "99line",
                "minResponseTime",
                "maxResponseTime",
                "avgBytes",
                "avgThroughput",
                "errorsRate"
            ]
        }
    },
    "request_id": "62b5d2071f481"
}
```
### Usuario y password incorrecto en login
Entradas:
```
curl --location --request GET 'https://a.blazemeter.com/api/v4/user' \
--header 'Authorization: Basic MTA4MTY5Mjc5ZmM2NzgyMDYxNjBhMGNjWFhYOmY1MmYzYmVjOWFhNGE5ZmVjYmI2ZTU2ZjQ4MjYyYjRlMjIzZTU4NjFlYjNjYmVlMDAyZjRjZjEyZjEyYzRkNmI0MTc0MzY1ZA==' \
--header 'Cookie: bzm_sess=3161f8cb2c07ec81e5459ccc1bb99d6a'
```
Salidas:
```
{
    "error": {
        "code": 401,
        "message": "Unauthorized"
    },
    "api_version": 4,
    "result": null,
    "request_id": "62b5d2379936b"
}
```
