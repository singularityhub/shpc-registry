---
layout: container
name:  "ghcr.io/autamus/unixodbc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/unixodbc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/unixodbc/container.yaml"
updated_at: "2023-10-10 03:16:43.876062"
latest: "2.3.4"
container_url: "https://github.com/orgs/autamus/packages/container/package/unixodbc"
aliases:
 - "odbc_config"
 - "odbcinst"
versions:
 - "2.3.4"
 - "latest"
description: "unixODBC-Test containing Qt based ODBC test tool, and autotest framework."
config: {"docker": "ghcr.io/autamus/unixodbc", "url": "https://github.com/orgs/autamus/packages/container/package/unixodbc", "maintainer": "@vsoch", "description": "unixODBC-Test containing Qt based ODBC test tool, and autotest framework.", "latest": {"2.3.4": "sha256:6f2a7eb8cba492f02ac83c1dd67e0cfaed157c120e0330db76153febc50d2e48"}, "tags": {"2.3.4": "sha256:6f2a7eb8cba492f02ac83c1dd67e0cfaed157c120e0330db76153febc50d2e48", "latest": "sha256:6f2a7eb8cba492f02ac83c1dd67e0cfaed157c120e0330db76153febc50d2e48"}, "aliases": {"odbc_config": "/opt/view/bin/odbc_config", "odbcinst": "/opt/view/bin/odbcinst"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/unixodbc.
unixODBC-Test containing Qt based ODBC test tool, and autotest framework.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/unixodbc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/unixodbc:2.3.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/unixodbc/2.3.4
$ module help ghcr.io/autamus/unixodbc/2.3.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unixodbc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unixodbc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unixodbc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unixodbc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unixodbc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unixodbc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### odbc_config

```bash
$ singularity exec <container> /opt/view/bin/odbc_config
$ podman run --it --rm --entrypoint /opt/view/bin/odbc_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/odbc_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odbcinst

```bash
$ singularity exec <container> /opt/view/bin/odbcinst
$ podman run --it --rm --entrypoint /opt/view/bin/odbcinst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/odbcinst   -v ${PWD} -w ${PWD} <container> -c " $@"
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