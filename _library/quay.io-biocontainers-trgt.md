---
layout: container
name:  "quay.io/biocontainers/trgt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trgt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trgt/container.yaml"
updated_at: "2025-12-08 04:15:14.075641"
latest: "4.0.0--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/trgt"
aliases:
 - "trgt"
 - "trvz"
versions:
 - "0.3.4--hdfd78af_0"
 - "0.4.0--hdfd78af_0"
 - "0.5.0--hdfd78af_0"
 - "0.7.0--hdfd78af_0"
 - "0.8.0--hdfd78af_0"
 - "0.9.0--hdfd78af_0"
 - "1.2.0--h9ee0642_0"
 - "1.1.0--h9ee0642_0"
 - "1.0.0--h9ee0642_0"
 - "1.4.1--h9ee0642_0"
 - "1.3.0--h9ee0642_0"
 - "2.0.0--h9ee0642_0"
 - "1.5.1--h9ee0642_0"
 - "3.0.0--h9ee0642_0"
 - "2.1.0--h9ee0642_0"
 - "4.0.0--h9ee0642_0"
description: "singularity registry hpc automated addition for trgt"
config: {"url": "https://biocontainers.pro/tools/trgt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for trgt", "latest": {"4.0.0--h9ee0642_0": "sha256:633e316ed683adec3026cea1448134f137693bc05b9025ec656ee23cf9229e14"}, "tags": {"0.3.4--hdfd78af_0": "sha256:fd43ea17e09f402bb0ee677021fc860a9308c081ec998cecf9030541b06a4aa7", "0.4.0--hdfd78af_0": "sha256:337aff680c8552224faefaa2f5bcedb7f7ec94ae585e085fc8ae4538c56b114d", "0.5.0--hdfd78af_0": "sha256:033eddc9aead1e2971c0a202f50eb642f708212a635f086cdb3cb9dc63752da1", "0.7.0--hdfd78af_0": "sha256:8630b3706c6fe0b25e8d8782cd4d02c1950b394a3b2eea6dbe3c7f0bfca670e9", "0.8.0--hdfd78af_0": "sha256:16d9c13b9be273013e76790df0e8421499fdc331ecab667726de2bb3f39d1918", "0.9.0--hdfd78af_0": "sha256:d64172ab796bac16e22e8e4527b0fdd304df3b7cc71356f8ad0a0dcabf3aa499", "1.2.0--h9ee0642_0": "sha256:87b351011a365419679271efb9cdf8c8d405521bf10132d6f1527167f7f3c4df", "1.1.0--h9ee0642_0": "sha256:c10ada4848c92d75ae1fb52b2a0182fb8dbde092dd9a78e4df287f47f1d69fef", "1.0.0--h9ee0642_0": "sha256:b09b469bcc140ca88aba0a4450f38d339c1377559454f43b340fe6aa95b2fca7", "1.4.1--h9ee0642_0": "sha256:f8d3083812bb7a47147d29bda275099db3bee329c459ae99ceb0ceff42811532", "1.3.0--h9ee0642_0": "sha256:92e55b1db16cc0b634305158eb8838e3ac19f80aba12de553a418147358c6953", "2.0.0--h9ee0642_0": "sha256:680ffeaf5a9cfd1754a893e787c2d53a34cb51abe1576178c43967cf688e69be", "1.5.1--h9ee0642_0": "sha256:d44833a32564fcc05c25e0e2065011e9f7ae4d51868cc9d5fb81c1f10c4516d9", "3.0.0--h9ee0642_0": "sha256:01a2017a2e6d89ce85827f31ffc8b0ec47848b8dd5a57bcfc3fb5bb65b37e811", "2.1.0--h9ee0642_0": "sha256:efc6e2f405019c537574cce39ee7d6042fe7686b0af2382b6fbcd59a3e7072da", "4.0.0--h9ee0642_0": "sha256:633e316ed683adec3026cea1448134f137693bc05b9025ec656ee23cf9229e14"}, "docker": "quay.io/biocontainers/trgt", "aliases": {"trgt": "/usr/local/bin/trgt", "trvz": "/usr/local/bin/trvz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trgt.
singularity registry hpc automated addition for trgt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trgt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trgt:4.0.0--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trgt/4.0.0--h9ee0642_0
$ module help quay.io/biocontainers/trgt/4.0.0--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trgt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trgt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trgt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trgt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trgt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trgt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trgt

```bash
$ singularity exec <container> /usr/local/bin/trgt
$ podman run --it --rm --entrypoint /usr/local/bin/trgt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trgt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trvz

```bash
$ singularity exec <container> /usr/local/bin/trvz
$ podman run --it --rm --entrypoint /usr/local/bin/trvz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trvz   -v ${PWD} -w ${PWD} <container> -c " $@"
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