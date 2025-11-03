---
layout: container
name:  "quay.io/biocontainers/treetime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/treetime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/treetime/container.yaml"
updated_at: "2025-11-03 04:09:00.935193"
latest: "0.11.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/treetime"
aliases:
 - "treetime"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.10"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.10"
versions:
 - "0.9.4--pyh7cba7a3_0"
 - "0.9.5--pyh7cba7a3_0"
 - "0.9.6--pyh7cba7a3_0"
 - "0.10.0--pyh7cba7a3_0"
 - "0.10.1--pyh7cba7a3_0"
 - "0.11.0--pyhdfd78af_0"
 - "0.11.1--pyhdfd78af_0"
 - "0.11.2--pyhdfd78af_0"
 - "0.11.3--pyhdfd78af_0"
 - "0.11.3--pyhdfd78af_1"
 - "0.11.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for treetime"
config: {"url": "https://biocontainers.pro/tools/treetime", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for treetime", "latest": {"0.11.4--pyhdfd78af_0": "sha256:f368effb33f05bf3c696ea42e3eb68abbbefb2435e30a2069c3f3929a11ff87f"}, "tags": {"0.9.4--pyh7cba7a3_0": "sha256:df33fd4fd5195a6b2346d5e2d33f56e00af8f2490ec094612d8895347c4f0be3", "0.9.5--pyh7cba7a3_0": "sha256:afd5467511dbc4a4385ebcd05ded2cfe697b22e4c374a7e2445d05fd11cb641c", "0.9.6--pyh7cba7a3_0": "sha256:580350cbb22cd283b9c519acaa3373b053b5df5b896ac96b59e89dc0de12e0fb", "0.10.0--pyh7cba7a3_0": "sha256:f736afcfc384845befcc0af0bea047a2ea63728b274bfaab2d36e72c7bfd0255", "0.10.1--pyh7cba7a3_0": "sha256:b54b9fbc03b32547fa6978769a30c145574c77c80410664e5bd1cf2240b369a2", "0.11.0--pyhdfd78af_0": "sha256:4992f0fb2fc90519c8508ce6293e1aefe697a20f7cb34179f991a7b38e4c7f79", "0.11.1--pyhdfd78af_0": "sha256:f252d4f707aecc58fe52a4403cea86e4da27d17f8cb3e436c0dc00599cf0071f", "0.11.2--pyhdfd78af_0": "sha256:3670f62f084344fc9ac8b5f700e82bcb17fc4b681c092f3b88324a9ab7dc96ba", "0.11.3--pyhdfd78af_0": "sha256:48d09c09508a3a3bb8cf6855cb71fdc3532d1b7389e49405b416f8041525b3d4", "0.11.3--pyhdfd78af_1": "sha256:5aaf5ae8beb2131be40f8d53ebbd688e8b293d3c6b759ad256b0108e25501105", "0.11.4--pyhdfd78af_0": "sha256:f368effb33f05bf3c696ea42e3eb68abbbefb2435e30a2069c3f3929a11ff87f"}, "docker": "quay.io/biocontainers/treetime", "aliases": {"treetime": "/usr/local/bin/treetime", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.10": "/usr/local/bin/2to3-3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/treetime.
shpc-registry automated BioContainers addition for treetime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/treetime
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/treetime:0.11.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/treetime/0.11.4--pyhdfd78af_0
$ module help quay.io/biocontainers/treetime/0.11.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### treetime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### treetime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### treetime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### treetime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### treetime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### treetime-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### treetime

```bash
$ singularity exec <container> /usr/local/bin/treetime
$ podman run --it --rm --entrypoint /usr/local/bin/treetime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treetime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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