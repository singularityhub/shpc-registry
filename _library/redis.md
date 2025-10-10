---
layout: container
name:  "redis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/redis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/redis/container.yaml"
updated_at: "2025-10-10 03:57:26.333695"
latest: "8-alpine3.22"
container_url: "https://hub.docker.com/r/_/redis"
aliases:
 - "redis-benchmark"
 - "redis-check-aof"
 - "redis-check-rdb"
 - "redis-cli"
 - "redis-sentinel"
 - "redis-server"
versions:
 - "6.2.3-alpine"
 - "6.2.4-alpine"
 - "6.2.5"
 - "6.2.6"
 - "7.0-rc"
 - "latest"
 - "6"
 - "6-alpine3.15"
 - "6.2"
 - "7"
 - "7-alpine3.15"
 - "7.0"
 - "7-alpine3.16"
 - "6-alpine3.16"
 - "7-alpine3.17"
 - "6-alpine3.17"
 - "7.2-rc"
 - "7-alpine3.18"
 - "7.2"
 - "7-alpine3.19"
 - "7-alpine3.20"
 - "7.4-rc"
 - "7.4"
 - "8.0-M01"
 - "8.0-M02"
 - "8.0-M03"
 - "7-alpine3.21"
 - "8.0-M04"
 - "8"
 - "8-alpine3.21"
 - "8.0"
 - "8.2-m01"
 - "8-alpine3.22"
 - "8.2"
 - "crane ls redis: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]"
description: "Redis is an open-source, networked, in-memory, key-value data store with optional durability."
config: {"docker": "redis", "url": "https://hub.docker.com/r/_/redis", "maintainer": "@vsoch", "description": "Redis is an open-source, networked, in-memory, key-value data store with optional durability.", "filter": ["^(?!.*32bit).*$"], "latest": {"8-alpine3.22": "crane digest redis:8-alpine3.22: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]"}, "tags": {"6.2.3-alpine": "crane digest redis:6.2.3-alpine: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6.2.4-alpine": "crane digest redis:6.2.4-alpine: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6.2.5": "crane digest redis:6.2.5: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6.2.6": "crane digest redis:6.2.6: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7.0-rc": "crane digest redis:7.0-rc: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "latest": "crane digest redis:latest: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6": "crane digest redis:6: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6-alpine3.15": "crane digest redis:6-alpine3.15: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6.2": "crane digest redis:6.2: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7": "crane digest redis:7: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7-alpine3.15": "crane digest redis:7-alpine3.15: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7.0": "crane digest redis:7.0: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7-alpine3.16": "crane digest redis:7-alpine3.16: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6-alpine3.16": "crane digest redis:6-alpine3.16: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7-alpine3.17": "crane digest redis:7-alpine3.17: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "6-alpine3.17": "crane digest redis:6-alpine3.17: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7.2-rc": "crane digest redis:7.2-rc: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7-alpine3.18": "crane digest redis:7-alpine3.18: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7.2": "crane digest redis:7.2: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7-alpine3.19": "crane digest redis:7-alpine3.19: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7-alpine3.20": "crane digest redis:7-alpine3.20: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7.4-rc": "crane digest redis:7.4-rc: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7.4": "crane digest redis:7.4: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8.0-M01": "crane digest redis:8.0-M01: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8.0-M02": "crane digest redis:8.0-M02: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8.0-M03": "crane digest redis:8.0-M03: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "7-alpine3.21": "crane digest redis:7-alpine3.21: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8.0-M04": "crane digest redis:8.0-M04: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8": "crane digest redis:8: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8-alpine3.21": "crane digest redis:8-alpine3.21: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8.0": "crane digest redis:8.0: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8.2-m01": "crane digest redis:8.2-m01: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8-alpine3.22": "crane digest redis:8-alpine3.22: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "8.2": "crane digest redis:8.2: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]", "crane ls redis: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]": "crane digest redis:crane ls redis: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]: parsing reference \"redis:crane ls redis: UNAUTHORIZED: authentication required; [map[Action:pull Class: Name:library/redis Type:repository]]\": could not parse reference"}, "aliases": {"redis-benchmark": "/usr/local/bin/redis-benchmark", "redis-check-aof": "/usr/local/bin/redis-check-aof", "redis-check-rdb": "/usr/local/bin/redis-check-rdb", "redis-cli": "/usr/local/bin/redis-cli", "redis-sentinel": "/usr/local/bin/redis-sentinel", "redis-server": "/usr/local/bin/redis-server"}}
---

This module is a singularity container wrapper for redis.
Redis is an open-source, networked, in-memory, key-value data store with optional durability.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install redis
```

Or a specific version:

```bash
$ shpc install redis:8-alpine3.22
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load redis/8-alpine3.22
$ module help redis/8-alpine3.22
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### redis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### redis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### redis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### redis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### redis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### redis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### redis-benchmark

```bash
$ singularity exec <container> /usr/local/bin/redis-benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/redis-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redis-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### redis-check-aof

```bash
$ singularity exec <container> /usr/local/bin/redis-check-aof
$ podman run --it --rm --entrypoint /usr/local/bin/redis-check-aof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redis-check-aof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### redis-check-rdb

```bash
$ singularity exec <container> /usr/local/bin/redis-check-rdb
$ podman run --it --rm --entrypoint /usr/local/bin/redis-check-rdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redis-check-rdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### redis-cli

```bash
$ singularity exec <container> /usr/local/bin/redis-cli
$ podman run --it --rm --entrypoint /usr/local/bin/redis-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redis-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### redis-sentinel

```bash
$ singularity exec <container> /usr/local/bin/redis-sentinel
$ podman run --it --rm --entrypoint /usr/local/bin/redis-sentinel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redis-sentinel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### redis-server

```bash
$ singularity exec <container> /usr/local/bin/redis-server
$ podman run --it --rm --entrypoint /usr/local/bin/redis-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/redis-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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