---
layout: container
name:  "solr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/solr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/solr/container.yaml"
updated_at: "2025-12-19 03:27:32.698171"
latest: "9.10"
container_url: "https://hub.docker.com/_/solr"
aliases:
 - "post"
 - "postlogs"
 - "solr"
versions:
 - "8.8.2-slim"
 - "8.9.0"
 - "8.9.0-slim"
 - "8.10.1"
 - "8.11.0"
 - "8.11.1"
 - "latest"
 - "8"
 - "8.11"
 - "8.10"
 - "8.9"
 - "8.8"
 - "9"
 - "9.0"
 - "9.1"
 - "9.2"
 - "9.3"
 - "9.4"
 - "9.5"
 - "9.6"
 - "9.7"
 - "9.8"
 - "9.9"
 - "9.10"
description: "Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene™."
config: {"docker": "solr", "url": "https://hub.docker.com/_/solr", "maintainer": "@vsoch", "description": "Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene\u2122.", "latest": {"9.10": "crane digest solr:9.10: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"8.8.2-slim": "sha256:c07b46b904443f7e07d9da00aa9feb91af0b54ba75bf1e1891916d3ed1ff8d9b", "8.9.0": "crane digest solr:8.9.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.9.0-slim": "crane digest solr:8.9.0-slim: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.10.1": "crane digest solr:8.10.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.11.0": "crane digest solr:8.11.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.11.1": "crane digest solr:8.11.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "latest": "crane digest solr:latest: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8": "crane digest solr:8: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.11": "crane digest solr:8.11: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.10": "crane digest solr:8.10: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.9": "crane digest solr:8.9: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "8.8": "crane digest solr:8.8: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9": "crane digest solr:9: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.0": "crane digest solr:9.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.1": "crane digest solr:9.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.2": "crane digest solr:9.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.3": "crane digest solr:9.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.4": "crane digest solr:9.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.5": "crane digest solr:9.5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.6": "crane digest solr:9.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.7": "crane digest solr:9.7: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.8": "crane digest solr:9.8: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.9": "crane digest solr:9.9: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "9.10": "crane digest solr:9.10: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "aliases": {"post": "/opt/solr/bin/post", "postlogs": "/opt/solr/bin/postlogs", "solr": "/opt/solr/bin/solr"}}
---

This module is a singularity container wrapper for solr.
Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene™.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install solr
```

Or a specific version:

```bash
$ shpc install solr:9.10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load solr/9.10
$ module help solr/9.10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### solr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### solr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### solr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### solr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### solr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### solr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### post

```bash
$ singularity exec <container> /opt/solr/bin/post
$ podman run --it --rm --entrypoint /opt/solr/bin/post   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/solr/bin/post   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### postlogs

```bash
$ singularity exec <container> /opt/solr/bin/postlogs
$ podman run --it --rm --entrypoint /opt/solr/bin/postlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/solr/bin/postlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### solr

```bash
$ singularity exec <container> /opt/solr/bin/solr
$ podman run --it --rm --entrypoint /opt/solr/bin/solr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/solr/bin/solr   -v ${PWD} -w ${PWD} <container> -c " $@"
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