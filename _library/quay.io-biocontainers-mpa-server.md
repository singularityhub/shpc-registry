---
layout: container
name:  "quay.io/biocontainers/mpa-server"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mpa-server/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mpa-server/container.yaml"
updated_at: "2025-12-19 05:20:46.422586"
latest: "3.4--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/mpa-server"
aliases:
 - "cpp"
 - "innochecksum"
 - "lz4_decompress"
 - "mpa-server"
 - "myisam_ftdump"
 - "myisamchk"
 - "myisamlog"
 - "myisampack"
 - "mysql"
 - "mysql.server"
 - "mysql_client_test"
 - "mysql_client_test_embedded"
 - "mysql_config_editor"
 - "mysql_embedded"
 - "mysql_install_db"
 - "mysql_plugin"
 - "mysql_secure_installation"
 - "mysql_ssl_rsa_setup"
 - "mysql_tzinfo_to_sql"
 - "mysql_upgrade"
 - "mysqladmin"
 - "mysqlbinlog"
 - "mysqlcheck"
 - "mysqld"
 - "mysqld_multi"
 - "mysqld_safe"
 - "mysqldump"
 - "mysqldumpslow"
 - "mysqlimport"
 - "mysqlpump"
 - "mysqlshow"
 - "mysqlslap"
 - "mysqltest"
 - "mysqltest_embedded"
 - "mysqlxtest"
 - "replace"
 - "resolve_stack_dump"
 - "resolveip"
 - "zlib_decompress"
 - "clhsdb"
 - "hsdb"
 - "perl5.32.0"
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
versions:
 - "3.4--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for mpa-server"
config: {"url": "https://biocontainers.pro/tools/mpa-server", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mpa-server", "latest": {"3.4--hdfd78af_3": "sha256:6d8f4119434b8222961e1dba4109b66b634c77708e2c31e17810b6a90ad0b338"}, "tags": {"3.4--hdfd78af_3": "sha256:6d8f4119434b8222961e1dba4109b66b634c77708e2c31e17810b6a90ad0b338"}, "docker": "quay.io/biocontainers/mpa-server", "aliases": {"cpp": "/usr/local/bin/cpp", "innochecksum": "/usr/local/bin/innochecksum", "lz4_decompress": "/usr/local/bin/lz4_decompress", "mpa-server": "/usr/local/bin/mpa-server", "myisam_ftdump": "/usr/local/bin/myisam_ftdump", "myisamchk": "/usr/local/bin/myisamchk", "myisamlog": "/usr/local/bin/myisamlog", "myisampack": "/usr/local/bin/myisampack", "mysql": "/usr/local/bin/mysql", "mysql.server": "/usr/local/bin/mysql.server", "mysql_client_test": "/usr/local/bin/mysql_client_test", "mysql_client_test_embedded": "/usr/local/bin/mysql_client_test_embedded", "mysql_config_editor": "/usr/local/bin/mysql_config_editor", "mysql_embedded": "/usr/local/bin/mysql_embedded", "mysql_install_db": "/usr/local/bin/mysql_install_db", "mysql_plugin": "/usr/local/bin/mysql_plugin", "mysql_secure_installation": "/usr/local/bin/mysql_secure_installation", "mysql_ssl_rsa_setup": "/usr/local/bin/mysql_ssl_rsa_setup", "mysql_tzinfo_to_sql": "/usr/local/bin/mysql_tzinfo_to_sql", "mysql_upgrade": "/usr/local/bin/mysql_upgrade", "mysqladmin": "/usr/local/bin/mysqladmin", "mysqlbinlog": "/usr/local/bin/mysqlbinlog", "mysqlcheck": "/usr/local/bin/mysqlcheck", "mysqld": "/usr/local/bin/mysqld", "mysqld_multi": "/usr/local/bin/mysqld_multi", "mysqld_safe": "/usr/local/bin/mysqld_safe", "mysqldump": "/usr/local/bin/mysqldump", "mysqldumpslow": "/usr/local/bin/mysqldumpslow", "mysqlimport": "/usr/local/bin/mysqlimport", "mysqlpump": "/usr/local/bin/mysqlpump", "mysqlshow": "/usr/local/bin/mysqlshow", "mysqlslap": "/usr/local/bin/mysqlslap", "mysqltest": "/usr/local/bin/mysqltest", "mysqltest_embedded": "/usr/local/bin/mysqltest_embedded", "mysqlxtest": "/usr/local/bin/mysqlxtest", "replace": "/usr/local/bin/replace", "resolve_stack_dump": "/usr/local/bin/resolve_stack_dump", "resolveip": "/usr/local/bin/resolveip", "zlib_decompress": "/usr/local/bin/zlib_decompress", "clhsdb": "/usr/local/bin/clhsdb", "hsdb": "/usr/local/bin/hsdb", "perl5.32.0": "/usr/local/bin/perl5.32.0", "my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mpa-server.
shpc-registry automated BioContainers addition for mpa-server
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mpa-server
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mpa-server:3.4--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mpa-server/3.4--hdfd78af_3
$ module help quay.io/biocontainers/mpa-server/3.4--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mpa-server-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mpa-server-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mpa-server-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mpa-server-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mpa-server-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mpa-server-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cpp

```bash
$ singularity exec <container> /usr/local/bin/cpp
$ podman run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### innochecksum

```bash
$ singularity exec <container> /usr/local/bin/innochecksum
$ podman run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/innochecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lz4_decompress

```bash
$ singularity exec <container> /usr/local/bin/lz4_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/lz4_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lz4_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpa-server

```bash
$ singularity exec <container> /usr/local/bin/mpa-server
$ podman run --it --rm --entrypoint /usr/local/bin/mpa-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpa-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisam_ftdump

```bash
$ singularity exec <container> /usr/local/bin/myisam_ftdump
$ podman run --it --rm --entrypoint /usr/local/bin/myisam_ftdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisam_ftdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisamchk

```bash
$ singularity exec <container> /usr/local/bin/myisamchk
$ podman run --it --rm --entrypoint /usr/local/bin/myisamchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisamchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisamlog

```bash
$ singularity exec <container> /usr/local/bin/myisamlog
$ podman run --it --rm --entrypoint /usr/local/bin/myisamlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisamlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myisampack

```bash
$ singularity exec <container> /usr/local/bin/myisampack
$ podman run --it --rm --entrypoint /usr/local/bin/myisampack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myisampack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql

```bash
$ singularity exec <container> /usr/local/bin/mysql
$ podman run --it --rm --entrypoint /usr/local/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql.server

```bash
$ singularity exec <container> /usr/local/bin/mysql.server
$ podman run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_client_test

```bash
$ singularity exec <container> /usr/local/bin/mysql_client_test
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_client_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_client_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_client_test_embedded

```bash
$ singularity exec <container> /usr/local/bin/mysql_client_test_embedded
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_client_test_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_client_test_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config_editor

```bash
$ singularity exec <container> /usr/local/bin/mysql_config_editor
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_embedded

```bash
$ singularity exec <container> /usr/local/bin/mysql_embedded
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_install_db

```bash
$ singularity exec <container> /usr/local/bin/mysql_install_db
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_install_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_install_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_plugin

```bash
$ singularity exec <container> /usr/local/bin/mysql_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_secure_installation

```bash
$ singularity exec <container> /usr/local/bin/mysql_secure_installation
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_ssl_rsa_setup

```bash
$ singularity exec <container> /usr/local/bin/mysql_ssl_rsa_setup
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_tzinfo_to_sql

```bash
$ singularity exec <container> /usr/local/bin/mysql_tzinfo_to_sql
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_upgrade

```bash
$ singularity exec <container> /usr/local/bin/mysql_upgrade
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqladmin

```bash
$ singularity exec <container> /usr/local/bin/mysqladmin
$ podman run --it --rm --entrypoint /usr/local/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlbinlog

```bash
$ singularity exec <container> /usr/local/bin/mysqlbinlog
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlcheck

```bash
$ singularity exec <container> /usr/local/bin/mysqlcheck
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld

```bash
$ singularity exec <container> /usr/local/bin/mysqld
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_multi

```bash
$ singularity exec <container> /usr/local/bin/mysqld_multi
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_safe

```bash
$ singularity exec <container> /usr/local/bin/mysqld_safe
$ podman run --it --rm --entrypoint /usr/local/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldump

```bash
$ singularity exec <container> /usr/local/bin/mysqldump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldumpslow

```bash
$ singularity exec <container> /usr/local/bin/mysqldumpslow
$ podman run --it --rm --entrypoint /usr/local/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlimport

```bash
$ singularity exec <container> /usr/local/bin/mysqlimport
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlpump

```bash
$ singularity exec <container> /usr/local/bin/mysqlpump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlshow

```bash
$ singularity exec <container> /usr/local/bin/mysqlshow
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlslap

```bash
$ singularity exec <container> /usr/local/bin/mysqlslap
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqltest

```bash
$ singularity exec <container> /usr/local/bin/mysqltest
$ podman run --it --rm --entrypoint /usr/local/bin/mysqltest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqltest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqltest_embedded

```bash
$ singularity exec <container> /usr/local/bin/mysqltest_embedded
$ podman run --it --rm --entrypoint /usr/local/bin/mysqltest_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqltest_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlxtest

```bash
$ singularity exec <container> /usr/local/bin/mysqlxtest
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlxtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlxtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### replace

```bash
$ singularity exec <container> /usr/local/bin/replace
$ podman run --it --rm --entrypoint /usr/local/bin/replace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/replace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resolve_stack_dump

```bash
$ singularity exec <container> /usr/local/bin/resolve_stack_dump
$ podman run --it --rm --entrypoint /usr/local/bin/resolve_stack_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/resolve_stack_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### resolveip

```bash
$ singularity exec <container> /usr/local/bin/resolveip
$ podman run --it --rm --entrypoint /usr/local/bin/resolveip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/resolveip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zlib_decompress

```bash
$ singularity exec <container> /usr/local/bin/zlib_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clhsdb

```bash
$ singularity exec <container> /usr/local/bin/clhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hsdb

```bash
$ singularity exec <container> /usr/local/bin/hsdb
$ podman run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
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