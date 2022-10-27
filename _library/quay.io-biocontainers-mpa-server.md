---
layout: container
name:  "quay.io/biocontainers/mpa-server"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mpa-server/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mpa-server/container.yaml"
updated_at: "2022-10-27 00:40:48.537940"
latest: "3.4--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/mpa-server"
aliases:
 - "cpp"
 - "lz4_decompress"
 - "mpa-server"
 - "mysql.server"
 - "mysql_client_test"
 - "mysql_client_test_embedded"
 - "mysql_config_editor"
 - "mysql_embedded"
 - "mysql_install_db"
 - "mysql_plugin"
 - "mysql_ssl_rsa_setup"
 - "mysqlpump"
 - "mysqltest"
 - "mysqltest_embedded"
 - "mysqlxtest"
 - "replace"
 - "resolve_stack_dump"
 - "resolveip"
 - "zlib_decompress"
versions:
 - "3.4--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for mpa-server"
config: {"url": "https://biocontainers.pro/tools/mpa-server", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mpa-server", "latest": {"3.4--hdfd78af_3": "sha256:6d8f4119434b8222961e1dba4109b66b634c77708e2c31e17810b6a90ad0b338"}, "tags": {"3.4--hdfd78af_3": "sha256:6d8f4119434b8222961e1dba4109b66b634c77708e2c31e17810b6a90ad0b338"}, "docker": "quay.io/biocontainers/mpa-server", "aliases": {"cpp": "/usr/local/bin/cpp", "lz4_decompress": "/usr/local/bin/lz4_decompress", "mpa-server": "/usr/local/bin/mpa-server", "mysql.server": "/usr/local/bin/mysql.server", "mysql_client_test": "/usr/local/bin/mysql_client_test", "mysql_client_test_embedded": "/usr/local/bin/mysql_client_test_embedded", "mysql_config_editor": "/usr/local/bin/mysql_config_editor", "mysql_embedded": "/usr/local/bin/mysql_embedded", "mysql_install_db": "/usr/local/bin/mysql_install_db", "mysql_plugin": "/usr/local/bin/mysql_plugin", "mysql_ssl_rsa_setup": "/usr/local/bin/mysql_ssl_rsa_setup", "mysqlpump": "/usr/local/bin/mysqlpump", "mysqltest": "/usr/local/bin/mysqltest", "mysqltest_embedded": "/usr/local/bin/mysqltest_embedded", "mysqlxtest": "/usr/local/bin/mysqlxtest", "replace": "/usr/local/bin/replace", "resolve_stack_dump": "/usr/local/bin/resolve_stack_dump", "resolveip": "/usr/local/bin/resolveip", "zlib_decompress": "/usr/local/bin/zlib_decompress"}}
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


#### mysql_ssl_rsa_setup

```bash
$ singularity exec <container> /usr/local/bin/mysql_ssl_rsa_setup
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlpump

```bash
$ singularity exec <container> /usr/local/bin/mysqlpump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
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