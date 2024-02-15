---
layout: container
name:  "solr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/solr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/solr/container.yaml"
updated_at: "2024-02-15 03:11:50.673716"
latest: "9.4"
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
description: "Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene™."
config: {"docker": "solr", "url": "https://hub.docker.com/_/solr", "maintainer": "@vsoch", "description": "Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene\u2122.", "latest": {"9.4": "sha256:287958e35dba2ce41bee1e1d359afe4fe21f97dfccc9d44a0dd9b2912562a7dd"}, "tags": {"8.8.2-slim": "sha256:c07b46b904443f7e07d9da00aa9feb91af0b54ba75bf1e1891916d3ed1ff8d9b", "8.9.0": "sha256:857cb9fadcc4dae9d20405d60eff3762a13b2bcfc33898628716df8f91b01ee8", "8.9.0-slim": "sha256:ab6fb88298782688b5932c761c16291efe3b46c63e3c16a72604b4a8c100dce0", "8.10.1": "sha256:dff43964cd5ca52199fe015a51bd2d1de37b8f82fbdeffaa266d4f9f7ef56fa7", "8.11.0": "sha256:66fe2feeba8c4afdea12c78a4f11218fadd81befc43f223a2f9267bf605a25d1", "8.11.1": "sha256:8c5f7881cebb283d8230203db2083eef2a64d604d0f6020d74de63e2645f0aec", "latest": "sha256:287958e35dba2ce41bee1e1d359afe4fe21f97dfccc9d44a0dd9b2912562a7dd", "8": "sha256:394f8cd63f7fd72398d7bae6ad933a80cc82b95ce1456ef8992db002da1513ed", "8.11": "sha256:394f8cd63f7fd72398d7bae6ad933a80cc82b95ce1456ef8992db002da1513ed", "8.10": "sha256:dff43964cd5ca52199fe015a51bd2d1de37b8f82fbdeffaa266d4f9f7ef56fa7", "8.9": "sha256:857cb9fadcc4dae9d20405d60eff3762a13b2bcfc33898628716df8f91b01ee8", "8.8": "sha256:cb946e325f1372b86b70dbdccc4f050655f63d9f678f645bf508088704349363", "9": "sha256:287958e35dba2ce41bee1e1d359afe4fe21f97dfccc9d44a0dd9b2912562a7dd", "9.0": "sha256:5103aea19a40a3462f612cd816d8ba6d0f58ff3ff5bf3930298393068797e83d", "9.1": "sha256:8e97c5151e169763c4f786dec78e48063fa74245dcab2650a446214553adb89f", "9.2": "sha256:c7d2485fb31e5acdda15c4b22fb9765d233875afd1bca51422dfc6ab7049748d", "9.3": "sha256:eddf2714d5d4ad039a8c3d2d928879e7ebfa01854d7e106b624c4a0a1cc11bd2", "9.4": "sha256:287958e35dba2ce41bee1e1d359afe4fe21f97dfccc9d44a0dd9b2912562a7dd"}, "aliases": {"post": "/opt/solr/bin/post", "postlogs": "/opt/solr/bin/postlogs", "solr": "/opt/solr/bin/solr"}}
---

This module is a singularity container wrapper for solr.
Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene™.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install solr
```

Or a specific version:

```bash
$ shpc install solr:9.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load solr/9.4
$ module help solr/9.4
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