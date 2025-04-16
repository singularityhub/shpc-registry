---
layout: container
name:  "quay.io/biocontainers/pxblat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pxblat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pxblat/container.yaml"
updated_at: "2025-04-16 03:19:19.048870"
latest: "1.2.1--py310h0dbaff4_0"
container_url: "https://biocontainers.pro/tools/pxblat"
aliases:
 - "pxblat"
 - "markdown-it"
 - "pygmentize"
 - "f2py3.10"
 - "htsfile"
 - "bgzip"
 - "tabix"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.10"
 - "python3.10-config"
 - "python3.1"
versions:
 - "0.2.0--py310hfb835a5_0"
 - "0.2.0--py39h1fb70d6_0"
 - "0.3.0--py311ha8d5032_0"
 - "0.3.2--py39h1fb70d6_0"
 - "0.3.4--py39h80cd5a4_0"
 - "1.1.10--py310h0dbaff4_0"
 - "1.0.0--py39h80cd5a4_0"
 - "0.3.10--py39h80cd5a4_1"
 - "1.1.20--py310h0dbaff4_0"
 - "1.1.20--py39h1f90b4d_0"
 - "1.0.0--py310hfcd7b35_0"
 - "0.3.10--py310hfcd7b35_1"
 - "1.2.1--py310h0dbaff4_0"
description: "singularity registry hpc automated addition for pxblat"
config: {"url": "https://biocontainers.pro/tools/pxblat", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pxblat", "latest": {"1.2.1--py310h0dbaff4_0": "sha256:17e45f72bb43cfd1d0a07b8923eea0a069456e5fb2bd5385b42c914461d1440f"}, "tags": {"0.2.0--py310hfb835a5_0": "sha256:b8c5e94848b1931754d6a32e21ff6b7d1b5ac7aa9ef18a31828bc0f492c886e4", "0.2.0--py39h1fb70d6_0": "sha256:9ad2e81e69c64c9f19d6d631e0be62aacecf0aef774fbd570e25e2d185808100", "0.3.0--py311ha8d5032_0": "sha256:65d926fc50f05a3944c24e9dc5d9ecfe7b1573446dc7329e3c5f8c35ee60c8eb", "0.3.2--py39h1fb70d6_0": "sha256:0a7b6f76112eafec5e740af221284715a24d5c6fdb38e2ddee7d7e5732ef1e96", "0.3.4--py39h80cd5a4_0": "sha256:f47dd29a0232905221b96a32c30ebaafbdd8505784b9566f2bf7aedb1f098bd2", "1.1.10--py310h0dbaff4_0": "sha256:857ce52fd0cd586b8459c608f49a046ad93e43ca7e6c6fa8d140884d7461d17f", "1.0.0--py39h80cd5a4_0": "sha256:4f0c5831ace810814d96419b6fcffe0b3e3a36ceecbb4e45a081b4db883cdc1b", "0.3.10--py39h80cd5a4_1": "sha256:2a9b0f62c1be86e77c4f69758c47f085af664935bbe5cb8f741417d989d2dabe", "1.1.20--py310h0dbaff4_0": "sha256:7537b8af981f3e7e3d3f0729978c7d1a9f96fe4d9d41511df1a4811dc29a0255", "1.1.20--py39h1f90b4d_0": "sha256:18c1fd99f6546e8806d6d3b36deb3a88de54fe1e1e3682a782e19f801f89a5f3", "1.0.0--py310hfcd7b35_0": "sha256:9156a38dab5668d91a50405f20ce52787b7fa9fbc1fada9e4fadf67ea98c2f17", "0.3.10--py310hfcd7b35_1": "sha256:45474e0de2c4670fcea30ad88f771ec34a6b62898148e235a1c1043bd7d3cc15", "1.2.1--py310h0dbaff4_0": "sha256:17e45f72bb43cfd1d0a07b8923eea0a069456e5fb2bd5385b42c914461d1440f"}, "docker": "quay.io/biocontainers/pxblat", "aliases": {"pxblat": "/usr/local/bin/pxblat", "markdown-it": "/usr/local/bin/markdown-it", "pygmentize": "/usr/local/bin/pygmentize", "f2py3.10": "/usr/local/bin/f2py3.10", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pxblat.
singularity registry hpc automated addition for pxblat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pxblat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pxblat:1.2.1--py310h0dbaff4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pxblat/1.2.1--py310h0dbaff4_0
$ module help quay.io/biocontainers/pxblat/1.2.1--py310h0dbaff4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pxblat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pxblat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pxblat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pxblat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pxblat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pxblat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pxblat

```bash
$ singularity exec <container> /usr/local/bin/pxblat
$ podman run --it --rm --entrypoint /usr/local/bin/pxblat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pxblat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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