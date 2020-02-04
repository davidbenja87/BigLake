
### RBAC - Role based Access Control

Manage Azure resources using RBAC

Three components in RBAC role assignment

Security Principal - User,Group,Service principal & Managed Identity
  This is used to identify their access to azure resources
  
Role definition
 - This is used to define their role /action with the resources

Scope

- This defines which area you have access to 

![](images/RBAC%20role%20assignment.PNG)

#### Role definition

In Role definition,we need to define our actions to perform on this resource

![Role definition](images/Role%20defination.PNG)

Like Role assignment, we also have deny assignment, this will take precendence over the role assignment.


Detailed document 


[RBAC document](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)


### Database scoped credential

Sql server/Datawarehouse can connect to external application like storage account by setting up Database scoped credential.

```sql
CREATE DATABASE SCOPED CREDENTIAL credential_name
WITH IDENTITY = 'identity_name'
    [ , SECRET = 'secret' ]
    
```    
    
Need to set up master key in the database to encrpyt secret provided in the Database scope credential

Detailed document
[Database scope credential](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-database-scoped-credential-transact-sql?view=sql-server-ver15)



