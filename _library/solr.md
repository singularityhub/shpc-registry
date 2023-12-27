---
layout: container
name:  "solr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/solr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/solr/container.yaml"
updated_at: "2023-12-27 02:25:26.113522"
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
config: {"docker": "solr", "url": "https://hub.docker.com/_/solr", "maintainer": "@vsoch", "description": "Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene\u2122.", "latest": {"9.4": "sha256:9e23dd3855e46c3e200fbcd4d11bd49c1bfc08955939504164127945af5aa686"}, "tags": {"8.8.2-slim": "sha256:c07b46b904443f7e07d9da00aa9feb91af0b54ba75bf1e1891916d3ed1ff8d9b", "8.9.0": "sha256:857cb9fadcc4dae9d20405d60eff3762a13b2bcfc33898628716df8f91b01ee8", "8.9.0-slim": "sha256:ab6fb88298782688b5932c761c16291efe3b46c63e3c16a72604b4a8c100dce0", "8.10.1": "sha256:dff43964cd5ca52199fe015a51bd2d1de37b8f82fbdeffaa266d4f9f7ef56fa7", "8.11.0": "sha256:66fe2feeba8c4afdea12c78a4f11218fadd81befc43f223a2f9267bf605a25d1", "8.11.1": "sha256:8c5f7881cebb283d8230203db2083eef2a64d604d0f6020d74de63e2645f0aec", "latest": "sha256:9e23dd3855e46c3e200fbcd4d11bd49c1bfc08955939504164127945af5aa686", "8": "sha256:a79b98cc1151f40623818f6c0a991e4653ee239d8d065a79c73ac464dc9565f2", "8.11": "sha256:a79b98cc1151f40623818f6c0a991e4653ee239d8d065a79c73ac464dc9565f2", "8.10": "sha256:dff43964cd5ca52199fe015a51bd2d1de37b8f82fbdeffaa266d4f9f7ef56fa7", "8.9": "sha256:857cb9fadcc4dae9d20405d60eff3762a13b2bcfc33898628716df8f91b01ee8", "8.8": "sha256:cb946e325f1372b86b70dbdccc4f050655f63d9f678f645bf508088704349363", "9": "sha256:9e23dd3855e46c3e200fbcd4d11bd49c1bfc08955939504164127945af5aa686", "9.0": "sha256:c8b13c0fc5dc563c1dff6d7699216f73b64ee8d77641dd88cd3e5a77fe424399", "9.1": "sha256:505212700deb36edc5db3e5cf2bb3e1aeea11625bad276fb0805cbf194239119", "9.2": "sha256:b6f00fb46ff8ef45444ac27ebbc6494a3ce2dcd80f176681589c2168bcabcb38", "9.3": "sha256:27961983bd535da16687f11f445d2da40d9bbb4d2e953838f750fba7a85e3f9c", "9.4": "sha256:9e23dd3855e46c3e200fbcd4d11bd49c1bfc08955939504164127945af5aa686"}, "aliases": {"post": "/opt/solr/bin/post", "postlogs": "/opt/solr/bin/postlogs", "solr": "/opt/solr/bin/solr"}}
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