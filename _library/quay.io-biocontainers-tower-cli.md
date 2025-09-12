---
layout: container
name:  "quay.io/biocontainers/tower-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tower-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tower-cli/container.yaml"
updated_at: "2025-09-12 02:58:32.736601"
latest: "0.14.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/tower-cli"
aliases:
 - "tw"
versions:
 - "0.8.0--h9ee0642_0"
 - "0.9.0--h9ee0642_0"
 - "0.9.2--hdfd78af_1"
 - "0.10.3--hdfd78af_0"
 - "0.10.3--hdfd78af_1"
 - "0.11.0--hdfd78af_0"
 - "0.11.1--hdfd78af_0"
 - "0.11.2--hdfd78af_0"
 - "0.11.5--hdfd78af_0"
 - "0.12.0--hdfd78af_0"
 - "0.13.0--hdfd78af_0"
 - "0.12.2--hdfd78af_0"
 - "0.14.0--hdfd78af_0"
description: "singularity registry hpc automated addition for tower-cli"
config: {"url": "https://biocontainers.pro/tools/tower-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for tower-cli", "latest": {"0.14.0--hdfd78af_0": "sha256:85b7dbae0ae8f36668b6ceda448db33ecb44bc0b4998fd7e5712541ab009dbdc"}, "tags": {"0.8.0--h9ee0642_0": "sha256:98825f778dd02b2803950474dbe80ffb3d0da267d98f65153ff2c2019c995eec", "0.9.0--h9ee0642_0": "sha256:f1933881b602f88c6a9960f5144afeb1413f41bc165a2ccf8e6bda913d11b7e2", "0.9.2--hdfd78af_1": "sha256:642a297b4932bdddad8c07851694e575b7968d3e127703fe232f5f347ada17ae", "0.10.3--hdfd78af_0": "sha256:78d4f142382a12021bb7056d8b63bff8ecda9a36c0c499f59350defa65f152cc", "0.10.3--hdfd78af_1": "sha256:5a4cdc53794f6869e361f1819bbb443f4aa6ed4eee9ba21286ea85f43db3c166", "0.11.0--hdfd78af_0": "sha256:1d135b2e2c1bc8026d8c3496e3fdf46fc16a29773a2fb6d777e49baab2faac67", "0.11.1--hdfd78af_0": "sha256:cde44a2520746c15640e2cdece7f9d5e049a445b1748f23c363ed8df87db86f6", "0.11.2--hdfd78af_0": "sha256:be88e58e3657c1b610129cee33a1d6e4937ee7074b307a62d356da39d2f6e1ab", "0.11.5--hdfd78af_0": "sha256:bfb971a912b14b294ce60dc985eb53992da375320e70cd07d82ba43f74fdb8a6", "0.12.0--hdfd78af_0": "sha256:620a9a9d00417e5f110ddbc3f49aea40cc5265e05e42f3497371dfd14be167ca", "0.13.0--hdfd78af_0": "sha256:f9668a1329a8e71fd4e184c70344991d352b7778b7d0615191cedd4c09bfe7e8", "0.12.2--hdfd78af_0": "sha256:cb156582705302be82371f6a21979e62066725f342d0ae063c1dad5402298b2b", "0.14.0--hdfd78af_0": "sha256:85b7dbae0ae8f36668b6ceda448db33ecb44bc0b4998fd7e5712541ab009dbdc"}, "docker": "quay.io/biocontainers/tower-cli", "aliases": {"tw": "/usr/local/bin/tw"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tower-cli.
singularity registry hpc automated addition for tower-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tower-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tower-cli:0.14.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tower-cli/0.14.0--hdfd78af_0
$ module help quay.io/biocontainers/tower-cli/0.14.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tower-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tower-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tower-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tower-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tower-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tower-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tw

```bash
$ singularity exec <container> /usr/local/bin/tw
$ podman run --it --rm --entrypoint /usr/local/bin/tw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tw   -v ${PWD} -w ${PWD} <container> -c " $@"
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