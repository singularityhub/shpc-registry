---
layout: container
name:  "quay.io/biocontainers/unikseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unikseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unikseq/container.yaml"
updated_at: "2025-12-09 04:03:07.230909"
latest: "2.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/unikseq"
aliases:
 - "LINKS"
 - "unikseq-Bloom.pl"
 - "unikseq.pl"
 - "writeBloom.pl"
versions:
 - "1.3.2--hdfd78af_0"
 - "1.3.3--hdfd78af_0"
 - "1.3.4--hdfd78af_0"
 - "1.3.5--hdfd78af_0"
 - "2.0.0--hdfd78af_0"
 - "2.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for unikseq"
config: {"url": "https://biocontainers.pro/tools/unikseq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unikseq", "latest": {"2.0.1--hdfd78af_0": "sha256:42a3999f450d1293418e8694cf636a815c8d5c74ca5f7a75c2a184e082e647cb"}, "tags": {"1.3.2--hdfd78af_0": "sha256:cf72f582501cb063b13685fde4036c209558fa01f92db54c90ceb0017d487ef2", "1.3.3--hdfd78af_0": "sha256:85eed2e9151faa711ff377ee13224c72a41fae2f7b82cb92e4aeb54c20598d72", "1.3.4--hdfd78af_0": "sha256:1fe91e5220db331e437954d19b827961b4f0e1f1e022490f0b51a81dadcd2c15", "1.3.5--hdfd78af_0": "sha256:215f1116256784fc9fd4d75292fed1a57007c507e5afa99dad37962c97108028", "2.0.0--hdfd78af_0": "sha256:eeff4bee2259eef463a720664fa4099fa1b12574eb18c0d0b9ca647346d8d993", "2.0.1--hdfd78af_0": "sha256:42a3999f450d1293418e8694cf636a815c8d5c74ca5f7a75c2a184e082e647cb"}, "docker": "quay.io/biocontainers/unikseq", "aliases": {"LINKS": "/usr/local/bin/LINKS", "unikseq-Bloom.pl": "/usr/local/bin/unikseq-Bloom.pl", "unikseq.pl": "/usr/local/bin/unikseq.pl", "writeBloom.pl": "/usr/local/bin/writeBloom.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unikseq.
singularity registry hpc automated addition for unikseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unikseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unikseq:2.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unikseq/2.0.1--hdfd78af_0
$ module help quay.io/biocontainers/unikseq/2.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unikseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unikseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unikseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unikseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unikseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unikseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LINKS

```bash
$ singularity exec <container> /usr/local/bin/LINKS
$ podman run --it --rm --entrypoint /usr/local/bin/LINKS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LINKS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unikseq-Bloom.pl

```bash
$ singularity exec <container> /usr/local/bin/unikseq-Bloom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/unikseq-Bloom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unikseq-Bloom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unikseq.pl

```bash
$ singularity exec <container> /usr/local/bin/unikseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/unikseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unikseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### writeBloom.pl

```bash
$ singularity exec <container> /usr/local/bin/writeBloom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/writeBloom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/writeBloom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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