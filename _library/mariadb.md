---
layout: container
name:  "mariadb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/mariadb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/mariadb/container.yaml"
updated_at: "2024-10-30 16:17:19.862641"
latest: "11-ubi9"
container_url: "https://hub.docker.com/r/_/mariadb"
aliases:
 - "mariabackup"
 - "mariadb"
 - "mariadb-access"
 - "mariadb-admin"
 - "mariadb-analyze"
 - "mariadb-backup"
 - "mariadb-binlog"
 - "mariadb-check"
 - "mariadb-conv"
 - "mariadb-convert-table-format"
 - "mariadb-dump"
 - "mariadb-dumpslow"
 - "mariadb-find-rows"
 - "mariadb-fix-extensions"
 - "mariadb-hotcopy"
 - "mariadb-import"
 - "mariadb-install-db"
 - "mariadb-optimize"
 - "mariadb-plugin"
 - "mariadb-repair"
 - "mariadb-report"
 - "mariadb-secure-installation"
 - "mariadb-service-convert"
 - "mariadb-setpermission"
 - "mariadb-show"
 - "mariadb-slap"
 - "mariadb-tzinfo-to-sql"
 - "mariadb-upgrade"
 - "mariadb-waitpid"
 - "mariadbcheck"
 - "mariadbd-multi"
 - "mariadbd-safe"
 - "mariadbd-safe-helper"
versions:
 - "10.5.9-focal"
 - "10.6.0-focal"
 - "10.6.1-focal"
 - "10.6.2-focal"
 - "10.6.3-focal"
 - "10.6.4"
 - "10.7.1"
 - "10.8.2"
 - "latest"
 - "10"
 - "10.8"
 - "10.7"
 - "10.6"
 - "10.5"
 - "10.9-rc"
 - "10.10-rc"
 - "10.9"
 - "10.11-rc"
 - "10.10"
 - "11.0-rc"
 - "10.11"
 - "11"
 - "11.1-rc"
 - "11.0"
 - "11.1"
 - "11.3-rc"
 - "11.2"
 - "11.4-rc"
 - "11.3"
 - "11-ubi9"
 - "11.5-noble-rc"
 - "11.4"
 - "11.6-noble-rc"
 - "11.5"
description: "MariaDB Server is one of the most popular database servers in the world. It’s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow."
config: {"docker": "mariadb", "url": "https://hub.docker.com/r/_/mariadb", "maintainer": "@vsoch", "description": "MariaDB Server is one of the most popular database servers in the world. It\u2019s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow.", "latest": {"11-ubi9": "sha256:a127f4c6c2df1feeed84ba9e9b7313a5761570c7a2767038bc821bfcfded691c"}, "tags": {"10.5.9-focal": "sha256:36288c675a192bd0a8a99cd6ba0780e31df85f0bfd0cbb204837cd108be3d236", "10.6.0-focal": "sha256:6b687eb768f01add603c1474003c62e13d130bfd7030ac5334c9ae6a73d09e0c", "10.6.1-focal": "sha256:b2ba2c4dcaf9a946241f7e368637d351a74010b58f7c5e50002b9735c95c6326", "10.6.2-focal": "sha256:a4ed26af22613745fc379e9e187290626d5b9297454cb6838709cf44a11b8ea5", "10.6.3-focal": "sha256:3b6f9fa1d406e168998d62501b2ee4f27d53138bebfcdac03540758996c5ff1d", "10.6.4": "sha256:c014ba1efc5dbd711d0520c7762d57807f35549de3414eb31e942a420c8a2ed2", "10.7.1": "sha256:5a8009369ee57c85b6f4a08406147bd9c505cde6b8250d16a27d2a5febfdead7", "10.8.2": "sha256:490f01279be1452f12f497a592112cb960cf0500938dbf0ea3f0135cb6728d3d", "latest": "sha256:712a4eac9f79d8ba5c4c2275573532edeb012573b1df84fb568d4e9d602f0340", "10": "sha256:5c2a279eacfa00bd4453b10569e36d8ee24331cdc09273df70c4dbd383c277b4", "10.8": "sha256:456709ab146585d6189da05669b84384518baecd83670c9e5221f8c20a47cf1e", "10.7": "sha256:9a48ac9f196f3d4fd6fea2cab59a49df9e7ca459bf14b2f7b85a0e38a5454571", "10.6": "sha256:baa61fd6d3fbd61c51f2d28b79f42c7e336e6a9f414938abe41d0062216b336a", "10.5": "sha256:4b0be45e2daf6e64c374d0bc7c6340289241bcd6756dd0a3cfeb20ceafdb8302", "10.9-rc": "sha256:d00abc105fbdab7240ccb963e878bd0417150861a3c13c487f45e3fe3d6eb7ee", "10.10-rc": "sha256:c01a0345c452d3c23496914be88dfb30603d4d3e25cf1f2e3804c8481f8cb9fa", "10.9": "sha256:56710811b0b96233ef84f4982d3337d88d3aa46a68f3fcb2853b94e1d04ea25c", "10.11-rc": "sha256:8a73cde6874a2466bdddf125f501ab23ebc3e2212410117a81e01811c8021ebc", "10.10": "sha256:334b315c10e5d0db1dc2305bfa27f7760335272a157364158dc30b10b70dfa9b", "11.0-rc": "sha256:f089f1f8cb28870fac8142ab02838e89ee1c0005d189155e0aa15fe51bab9371", "10.11": "sha256:5c2a279eacfa00bd4453b10569e36d8ee24331cdc09273df70c4dbd383c277b4", "11": "sha256:712a4eac9f79d8ba5c4c2275573532edeb012573b1df84fb568d4e9d602f0340", "11.1-rc": "sha256:a104070983c2a9ab542d6142de858457dd15d2cabd7ac26e4ca3891d7721e73e", "11.0": "sha256:9f56b2ac10055b68d07e3dcf2a17109fef77f1f08d504b1f028eb874457963b6", "11.1": "sha256:6f42bfc1b0ceacc22c49c1e934f6ed68c4cec658f199101dc0c8d45f3b90941d", "11.3-rc": "sha256:bad88bdb821d02f4dee82225b654bf2f4507e8c8107ee34109a7f8517a115707", "11.2": "sha256:1363d4688aed0a0c3ddacb6e1b0a93dcfd765e557cb05e207b46bc8c60e376af", "11.4-rc": "sha256:3bf8ed1365f8ed10ebd2e66a8f389d0bc0b16f0951a4e4316e881105aa9291a4", "11.3": "sha256:e101f9db31916a5d4d7d594dd0dd092fb23ab4f499f1d7a7425d1afd4162c4bc", "11-ubi9": "sha256:a127f4c6c2df1feeed84ba9e9b7313a5761570c7a2767038bc821bfcfded691c", "11.5-noble-rc": "sha256:a67640489ba0d28f38a8f5e7880d4c6edd578cfdfca3f1fc06bef21b2d67d6b9", "11.4": "sha256:2002fb1acaf50e113aa3b37064cabb389721c1ac5348bb0e3f3a686b28cb618d", "11.6-noble-rc": "sha256:90dfad9a120e1293cdc142b59f3b727fc7819a02064d55791c6439b8eaca30e6", "11.5": "sha256:712a4eac9f79d8ba5c4c2275573532edeb012573b1df84fb568d4e9d602f0340"}, "aliases": {"mariabackup": "/usr/bin/mariabackup", "mariadb": "/usr/bin/mariadb", "mariadb-access": "/usr/bin/mariadb-access", "mariadb-admin": "/usr/bin/mariadb-admin", "mariadb-analyze": "/usr/bin/mariadb-analyze", "mariadb-backup": "/usr/bin/mariadb-backup", "mariadb-binlog": "/usr/bin/mariadb-binlog", "mariadb-check": "/usr/bin/mariadb-check", "mariadb-conv": "/usr/bin/mariadb-conv", "mariadb-convert-table-format": "/usr/bin/mariadb-convert-table-format", "mariadb-dump": "/usr/bin/mariadb-dump", "mariadb-dumpslow": "/usr/bin/mariadb-dumpslow", "mariadb-find-rows": "/usr/bin/mariadb-find-rows", "mariadb-fix-extensions": "/usr/bin/mariadb-fix-extensions", "mariadb-hotcopy": "/usr/bin/mariadb-hotcopy", "mariadb-import": "/usr/bin/mariadb-import", "mariadb-install-db": "/usr/bin/mariadb-install-db", "mariadb-optimize": "/usr/bin/mariadb-optimize", "mariadb-plugin": "/usr/bin/mariadb-plugin", "mariadb-repair": "/usr/bin/mariadb-repair", "mariadb-report": "/usr/bin/mariadb-report", "mariadb-secure-installation": "/usr/bin/mariadb-secure-installation", "mariadb-service-convert": "/usr/bin/mariadb-service-convert", "mariadb-setpermission": "/usr/bin/mariadb-setpermission", "mariadb-show": "/usr/bin/mariadb-show", "mariadb-slap": "/usr/bin/mariadb-slap", "mariadb-tzinfo-to-sql": "/usr/bin/mariadb-tzinfo-to-sql", "mariadb-upgrade": "/usr/bin/mariadb-upgrade", "mariadb-waitpid": "/usr/bin/mariadb-waitpid", "mariadbcheck": "/usr/bin/mariadbcheck", "mariadbd-multi": "/usr/bin/mariadbd-multi", "mariadbd-safe": "/usr/bin/mariadbd-safe", "mariadbd-safe-helper": "/usr/bin/mariadbd-safe-helper"}}
---

This module is a singularity container wrapper for mariadb.
MariaDB Server is one of the most popular database servers in the world. It’s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install mariadb
```

Or a specific version:

```bash
$ shpc install mariadb:11-ubi9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mariadb/11-ubi9
$ module help mariadb/11-ubi9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mariadb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mariadb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mariadb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mariadb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mariadb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mariadb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mariabackup

```bash
$ singularity exec <container> /usr/bin/mariabackup
$ podman run --it --rm --entrypoint /usr/bin/mariabackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariabackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb

```bash
$ singularity exec <container> /usr/bin/mariadb
$ podman run --it --rm --entrypoint /usr/bin/mariadb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-access

```bash
$ singularity exec <container> /usr/bin/mariadb-access
$ podman run --it --rm --entrypoint /usr/bin/mariadb-access   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-access   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-admin

```bash
$ singularity exec <container> /usr/bin/mariadb-admin
$ podman run --it --rm --entrypoint /usr/bin/mariadb-admin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-admin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-analyze

```bash
$ singularity exec <container> /usr/bin/mariadb-analyze
$ podman run --it --rm --entrypoint /usr/bin/mariadb-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-backup

```bash
$ singularity exec <container> /usr/bin/mariadb-backup
$ podman run --it --rm --entrypoint /usr/bin/mariadb-backup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-backup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-binlog

```bash
$ singularity exec <container> /usr/bin/mariadb-binlog
$ podman run --it --rm --entrypoint /usr/bin/mariadb-binlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-binlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-check

```bash
$ singularity exec <container> /usr/bin/mariadb-check
$ podman run --it --rm --entrypoint /usr/bin/mariadb-check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-conv

```bash
$ singularity exec <container> /usr/bin/mariadb-conv
$ podman run --it --rm --entrypoint /usr/bin/mariadb-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-conv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-convert-table-format

```bash
$ singularity exec <container> /usr/bin/mariadb-convert-table-format
$ podman run --it --rm --entrypoint /usr/bin/mariadb-convert-table-format   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-convert-table-format   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-dump

```bash
$ singularity exec <container> /usr/bin/mariadb-dump
$ podman run --it --rm --entrypoint /usr/bin/mariadb-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-dumpslow

```bash
$ singularity exec <container> /usr/bin/mariadb-dumpslow
$ podman run --it --rm --entrypoint /usr/bin/mariadb-dumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-dumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-find-rows

```bash
$ singularity exec <container> /usr/bin/mariadb-find-rows
$ podman run --it --rm --entrypoint /usr/bin/mariadb-find-rows   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-find-rows   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-fix-extensions

```bash
$ singularity exec <container> /usr/bin/mariadb-fix-extensions
$ podman run --it --rm --entrypoint /usr/bin/mariadb-fix-extensions   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-fix-extensions   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-hotcopy

```bash
$ singularity exec <container> /usr/bin/mariadb-hotcopy
$ podman run --it --rm --entrypoint /usr/bin/mariadb-hotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-hotcopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-import

```bash
$ singularity exec <container> /usr/bin/mariadb-import
$ podman run --it --rm --entrypoint /usr/bin/mariadb-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-install-db

```bash
$ singularity exec <container> /usr/bin/mariadb-install-db
$ podman run --it --rm --entrypoint /usr/bin/mariadb-install-db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-install-db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-optimize

```bash
$ singularity exec <container> /usr/bin/mariadb-optimize
$ podman run --it --rm --entrypoint /usr/bin/mariadb-optimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-optimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-plugin

```bash
$ singularity exec <container> /usr/bin/mariadb-plugin
$ podman run --it --rm --entrypoint /usr/bin/mariadb-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-repair

```bash
$ singularity exec <container> /usr/bin/mariadb-repair
$ podman run --it --rm --entrypoint /usr/bin/mariadb-repair   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-repair   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-report

```bash
$ singularity exec <container> /usr/bin/mariadb-report
$ podman run --it --rm --entrypoint /usr/bin/mariadb-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-secure-installation

```bash
$ singularity exec <container> /usr/bin/mariadb-secure-installation
$ podman run --it --rm --entrypoint /usr/bin/mariadb-secure-installation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-secure-installation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-service-convert

```bash
$ singularity exec <container> /usr/bin/mariadb-service-convert
$ podman run --it --rm --entrypoint /usr/bin/mariadb-service-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-service-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-setpermission

```bash
$ singularity exec <container> /usr/bin/mariadb-setpermission
$ podman run --it --rm --entrypoint /usr/bin/mariadb-setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-setpermission   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-show

```bash
$ singularity exec <container> /usr/bin/mariadb-show
$ podman run --it --rm --entrypoint /usr/bin/mariadb-show   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-show   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-slap

```bash
$ singularity exec <container> /usr/bin/mariadb-slap
$ podman run --it --rm --entrypoint /usr/bin/mariadb-slap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-slap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-tzinfo-to-sql

```bash
$ singularity exec <container> /usr/bin/mariadb-tzinfo-to-sql
$ podman run --it --rm --entrypoint /usr/bin/mariadb-tzinfo-to-sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-tzinfo-to-sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-upgrade

```bash
$ singularity exec <container> /usr/bin/mariadb-upgrade
$ podman run --it --rm --entrypoint /usr/bin/mariadb-upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadb-waitpid

```bash
$ singularity exec <container> /usr/bin/mariadb-waitpid
$ podman run --it --rm --entrypoint /usr/bin/mariadb-waitpid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadb-waitpid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadbcheck

```bash
$ singularity exec <container> /usr/bin/mariadbcheck
$ podman run --it --rm --entrypoint /usr/bin/mariadbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadbd-multi

```bash
$ singularity exec <container> /usr/bin/mariadbd-multi
$ podman run --it --rm --entrypoint /usr/bin/mariadbd-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadbd-multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadbd-safe

```bash
$ singularity exec <container> /usr/bin/mariadbd-safe
$ podman run --it --rm --entrypoint /usr/bin/mariadbd-safe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadbd-safe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mariadbd-safe-helper

```bash
$ singularity exec <container> /usr/bin/mariadbd-safe-helper
$ podman run --it --rm --entrypoint /usr/bin/mariadbd-safe-helper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mariadbd-safe-helper   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)