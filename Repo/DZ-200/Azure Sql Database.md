## Azure sql database

Azure sql database is a database PAAS service.


#### Data encryption

##### Always encrypted

Encrypts data at rest, motion (transfer between client and server) and in use (RAM).

Always encrypted ensures that you never see the plain text in the database until unless you have access to the Column master key (CMK) & Column encryption key(CEK).

Store the keys in Azure key vault/ windows certificate store.

There are two type of encryption method
 * Deterministic
   The same value should be encrypted with same encrypted value. This is useful for lookup, joining and filtering.
 * Random
   It produces the different encrypted value for the same column value.
   
   
   Steps to encrypt column
   
   * Set up azure key vault
   * set up database and table
   * configure service principal or user to access the key value with the right access policy - get,list,wrap,unwrap.
   * configure the field required to encrypt by specifing the encrypted method and encryted algorithm (CEK)
   * configure the store(Keyvault / windows store) to save CMK.
   
   


