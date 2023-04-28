---
layout: container
name:  "mariadb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/mariadb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/mariadb/container.yaml"
updated_at: "2023-04-28 02:33:50.758170"
latest: "11.0-rc"
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
description: "MariaDB Server is one of the most popular database servers in the world. It’s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow."
config: {"docker": "mariadb", "url": "https://hub.docker.com/r/_/mariadb", "maintainer": "@vsoch", "description": "MariaDB Server is one of the most popular database servers in the world. It\u2019s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow.", "latest": {"11.0-rc": "sha256:bb881d327e1bf297008ed88958de0bcb88ff58586c1f5e81d82a602ae5ab7967"}, "tags": {"10.5.9-focal": "sha256:36288c675a192bd0a8a99cd6ba0780e31df85f0bfd0cbb204837cd108be3d236", "10.6.0-focal": "sha256:6b687eb768f01add603c1474003c62e13d130bfd7030ac5334c9ae6a73d09e0c", "10.6.1-focal": "sha256:b2ba2c4dcaf9a946241f7e368637d351a74010b58f7c5e50002b9735c95c6326", "10.6.2-focal": "sha256:a4ed26af22613745fc379e9e187290626d5b9297454cb6838709cf44a11b8ea5", "10.6.3-focal": "sha256:3b6f9fa1d406e168998d62501b2ee4f27d53138bebfcdac03540758996c5ff1d", "10.6.4": "sha256:c014ba1efc5dbd711d0520c7762d57807f35549de3414eb31e942a420c8a2ed2", "10.7.1": "sha256:5a8009369ee57c85b6f4a08406147bd9c505cde6b8250d16a27d2a5febfdead7", "10.8.2": "sha256:490f01279be1452f12f497a592112cb960cf0500938dbf0ea3f0135cb6728d3d", "latest": "sha256:9ff479f244cc596aed9794d035a9f352662f2caed933238c533024df64569853", "10": "sha256:9ff479f244cc596aed9794d035a9f352662f2caed933238c533024df64569853", "10.8": "sha256:ac65f8db1d8f869e6e1254b82db35042356449ee1df9b4f7f44bc8085bc5b476", "10.7": "sha256:848dfb9c5ac4f261c3b74a56aa9f1c5b2cbe8157ce026442c2d4c8f8dfd9b393", "10.6": "sha256:0417aaccc8ba1dca8fbedb4c6a8e4786b7fc8492f6c5c741986d51f49eedad93", "10.5": "sha256:0bb77e477553bf157e6fda27d62bbc948144497b15f2e878bde5592d333043b2", "10.9-rc": "sha256:d00abc105fbdab7240ccb963e878bd0417150861a3c13c487f45e3fe3d6eb7ee", "10.10-rc": "sha256:c01a0345c452d3c23496914be88dfb30603d4d3e25cf1f2e3804c8481f8cb9fa", "10.9": "sha256:f585e5e6881b7b58c500d768c78fcd19541fede2a3c5d729c49bb1f237db1bca", "10.11-rc": "sha256:8a73cde6874a2466bdddf125f501ab23ebc3e2212410117a81e01811c8021ebc", "10.10": "sha256:ffdfe63ed2d80a32bab5c417f9233b23ddc0d0ffe699fecc570ecf3c05e39f86", "11.0-rc": "sha256:bb881d327e1bf297008ed88958de0bcb88ff58586c1f5e81d82a602ae5ab7967", "10.11": "sha256:9ff479f244cc596aed9794d035a9f352662f2caed933238c533024df64569853"}, "aliases": {"mariabackup": "/usr/bin/mariabackup", "mariadb": "/usr/bin/mariadb", "mariadb-access": "/usr/bin/mariadb-access", "mariadb-admin": "/usr/bin/mariadb-admin", "mariadb-analyze": "/usr/bin/mariadb-analyze", "mariadb-backup": "/usr/bin/mariadb-backup", "mariadb-binlog": "/usr/bin/mariadb-binlog", "mariadb-check": "/usr/bin/mariadb-check", "mariadb-conv": "/usr/bin/mariadb-conv", "mariadb-convert-table-format": "/usr/bin/mariadb-convert-table-format", "mariadb-dump": "/usr/bin/mariadb-dump", "mariadb-dumpslow": "/usr/bin/mariadb-dumpslow", "mariadb-find-rows": "/usr/bin/mariadb-find-rows", "mariadb-fix-extensions": "/usr/bin/mariadb-fix-extensions", "mariadb-hotcopy": "/usr/bin/mariadb-hotcopy", "mariadb-import": "/usr/bin/mariadb-import", "mariadb-install-db": "/usr/bin/mariadb-install-db", "mariadb-optimize": "/usr/bin/mariadb-optimize", "mariadb-plugin": "/usr/bin/mariadb-plugin", "mariadb-repair": "/usr/bin/mariadb-repair", "mariadb-report": "/usr/bin/mariadb-report", "mariadb-secure-installation": "/usr/bin/mariadb-secure-installation", "mariadb-service-convert": "/usr/bin/mariadb-service-convert", "mariadb-setpermission": "/usr/bin/mariadb-setpermission", "mariadb-show": "/usr/bin/mariadb-show", "mariadb-slap": "/usr/bin/mariadb-slap", "mariadb-tzinfo-to-sql": "/usr/bin/mariadb-tzinfo-to-sql", "mariadb-upgrade": "/usr/bin/mariadb-upgrade", "mariadb-waitpid": "/usr/bin/mariadb-waitpid", "mariadbcheck": "/usr/bin/mariadbcheck", "mariadbd-multi": "/usr/bin/mariadbd-multi", "mariadbd-safe": "/usr/bin/mariadbd-safe", "mariadbd-safe-helper": "/usr/bin/mariadbd-safe-helper"}}
---

This module is a singularity container wrapper for mariadb.
MariaDB Server is one of the most popular database servers in the world. It’s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install mariadb
```

Or a specific version:

```bash
$ shpc install mariadb:11.0-rc
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mariadb/11.0-rc
$ module help mariadb/11.0-rc
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