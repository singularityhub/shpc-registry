---
layout: container
name:  "quay.io/biocontainers/kleborate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kleborate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kleborate/container.yaml"
updated_at: "2023-07-31 03:33:10.837859"
latest: "2.3.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/kleborate"
aliases:
 - "kaptive.py"
 - "kleborate"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
 - "capnpc-capnp"
 - "mash"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
versions:
 - "2.2.0--pyhdfd78af_0"
 - "2.3.1--pyhdfd78af_0"
 - "2.3.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for kleborate"
config: {"url": "https://biocontainers.pro/tools/kleborate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kleborate", "latest": {"2.3.2--pyhdfd78af_0": "sha256:8400ad100395918f249cd1f63c00be7fa361881baad46379c21664f0771d6609"}, "tags": {"2.2.0--pyhdfd78af_0": "sha256:503a97f3531f59af5511a1f619ea3a0f4e0d2e5f714f99a30e3a9797be09b19d", "2.3.1--pyhdfd78af_0": "sha256:59c62701bb1013da74c4a758ddd63e15468f02dc0b8f8bb9f480673b8ab8daba", "2.3.2--pyhdfd78af_0": "sha256:8400ad100395918f249cd1f63c00be7fa361881baad46379c21664f0771d6609"}, "docker": "quay.io/biocontainers/kleborate", "aliases": {"kaptive.py": "/usr/local/bin/kaptive.py", "kleborate": "/usr/local/bin/kleborate", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++", "capnpc-capnp": "/usr/local/bin/capnpc-capnp", "mash": "/usr/local/bin/mash", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kleborate.
shpc-registry automated BioContainers addition for kleborate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kleborate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kleborate:2.3.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kleborate/2.3.2--pyhdfd78af_0
$ module help quay.io/biocontainers/kleborate/2.3.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kleborate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kleborate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kleborate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kleborate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kleborate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kleborate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kaptive.py

```bash
$ singularity exec <container> /usr/local/bin/kaptive.py
$ podman run --it --rm --entrypoint /usr/local/bin/kaptive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaptive.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kleborate

```bash
$ singularity exec <container> /usr/local/bin/kleborate
$ podman run --it --rm --entrypoint /usr/local/bin/kleborate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kleborate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-c++

```bash
$ singularity exec <container> /usr/local/bin/capnpc-c++
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-capnp

```bash
$ singularity exec <container> /usr/local/bin/capnpc-capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mash

```bash
$ singularity exec <container> /usr/local/bin/mash
$ podman run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
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