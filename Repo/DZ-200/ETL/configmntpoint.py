# Databricks notebook source
SasURL = 'https://mylearndatabricksstore.blob.core.windows.net/?sv=2019-02-02&ss=bfqt&srt=sco&sp=rwdlacup&se=2020-01-11T17:32:52Z&st=2019-12-23T09:32:52Z&spr=https&sig=4ao1O6EMXBz2kNdTQ7XCt7WV1U02lYd2olIIwsl2gGU%3D'
indQuestionMark = SasURL.index('?')
SasKey = SasURL[indQuestionMark:len(SasURL)]
StorageAccount = "mylearndatabricksstore"
ContainerName = "labdata"
MountPoint = "/mnt/dw-training"

dbutils.fs.mount(
  source = "wasbs://%s@%s.blob.core.windows.net/" % (ContainerName, StorageAccount),
  mount_point = MountPoint,
  extra_configs = {"fs.azure.sas.%s.%s.blob.core.windows.net" % (ContainerName, StorageAccount) : "%s" % SasKey}
)
