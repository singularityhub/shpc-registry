---
layout: container
name:  "quay.io/biocontainers/r-goalie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-goalie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-goalie/container.yaml"
updated_at: "2025-04-16 03:13:09.003477"
latest: "0.7.8--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-goalie"

versions:
 - "0.6.0--r41hdfd78af_0"
 - "0.6.6--r42hdfd78af_1"
 - "0.6.7--r42hdfd78af_0"
 - "0.6.8--r42hdfd78af_0"
 - "0.6.8--r42hdfd78af_1"
 - "0.6.9--r42hdfd78af_1"
 - "0.6.10--r42hdfd78af_0"
 - "0.6.11--r43hdfd78af_0"
 - "0.7.7--r43hdfd78af_1"
 - "0.6.18--r43hdfd78af_0"
 - "0.7.7--r44hdfd78af_2"
 - "0.7.8--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-goalie"
config: {"url": "https://biocontainers.pro/tools/r-goalie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-goalie", "latest": {"0.7.8--r44hdfd78af_0": "sha256:2943a3d12ed9161f9afd9812a17dd91c1891f387cb5861feed2aa8890c3e111c"}, "tags": {"0.6.0--r41hdfd78af_0": "sha256:a325da85dec2f4b653c6b77314852291f8a6384534a21cc0bab715e4d9581f38", "0.6.6--r42hdfd78af_1": "sha256:b5b8d73740d55553148c7de88b54315d0a5ba843ba468b7fd408f99a72635be2", "0.6.7--r42hdfd78af_0": "sha256:fadea0235c03e420a43588fc7850bde802eb6d0336decf17e909a4a0e6c0f7c7", "0.6.8--r42hdfd78af_0": "sha256:de3733dd01c8694d1c72c3cac290438c0267c8b835124ed809190e7ac7b19d1c", "0.6.8--r42hdfd78af_1": "sha256:33c940b37e0bb54d35f9010994d4c05e3acd1c281bf04b9fb947b4a80c2add59", "0.6.9--r42hdfd78af_1": "sha256:732de7c1c7e6ed903137841bea50da7ee959599df17a1b0b2015cea1e82cc235", "0.6.10--r42hdfd78af_0": "sha256:3ff95d0918f0b64beed0ddbc4924d5dee039b919e67eafbd9075fff47a045dc1", "0.6.11--r43hdfd78af_0": "sha256:49c3d51bd88e443ad636e3c3ea23daa2d13381c2a649153bb721098778a4bd7a", "0.7.7--r43hdfd78af_1": "sha256:c1de67897e7ceeb021099186a56ded72eda24e28f670ff6aced1659ed59a7e80", "0.6.18--r43hdfd78af_0": "sha256:e39f04e173b7b412692e13bb631313f5fb3538999b787fe5ee825df2dd6bb01e", "0.7.7--r44hdfd78af_2": "sha256:46459919aea17a7eee410bea454b5cf87a4d4cce6ffd387ba573f78ae94df098", "0.7.8--r44hdfd78af_0": "sha256:2943a3d12ed9161f9afd9812a17dd91c1891f387cb5861feed2aa8890c3e111c"}, "docker": "quay.io/biocontainers/r-goalie"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-goalie.
shpc-registry automated BioContainers addition for r-goalie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-goalie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-goalie:0.7.8--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-goalie/0.7.8--r44hdfd78af_0
$ module help quay.io/biocontainers/r-goalie/0.7.8--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-goalie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-goalie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-goalie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-goalie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-goalie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-goalie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-goalie

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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