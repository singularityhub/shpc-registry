---
layout: container
name:  "quay.io/biocontainers/nf-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nf-core/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nf-core/container.yaml"
updated_at: "2024-05-11 02:49:38.078553"
latest: "2.13.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nf-core"
aliases:
 - "cheetah"
 - "cheetah-analyze"
 - "cheetah-compile"
 - "galaxy-tool-test"
 - "import_igenome"
 - "mulled-build"
 - "mulled-build-channel"
 - "mulled-build-files"
 - "mulled-build-tool"
 - "mulled-hash"
 - "mulled-list"
 - "mulled-search"
 - "mulled-update-singularity-containers"
 - "nf-core"
 - "refgenie"
 - "rich-click"
 - "scalar"
 - "conda-env"
 - "cph"
 - "git"
 - "git-cvsserver"
 - "git-receive-pack"
 - "git-shell"
 - "git-upload-archive"
 - "git-upload-pack"
 - "gitk"
 - "docutils"
versions:
 - "2.6--pyh7cba7a3_1"
 - "2.7.2--pyh7cba7a3_0"
 - "2.8--pyh7cba7a3_0"
 - "2.9--pyh7cba7a3_0"
 - "2.10--pyhdfd78af_0"
 - "2.11.1--pyhdfd78af_0"
 - "2.12.1--pyhdfd78af_0"
 - "2.13.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for nf-core"
config: {"url": "https://biocontainers.pro/tools/nf-core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nf-core", "latest": {"2.13.1--pyhdfd78af_0": "sha256:47a4f78725aa736d712bd1f0e7bd38de0bdc32daf942dace1e8bc1565c822a1e"}, "tags": {"2.6--pyh7cba7a3_1": "sha256:e93a47ded9e18567f695e8610846f32f935c1db44ac5c5b03ab51ece3e8c5735", "2.7.2--pyh7cba7a3_0": "sha256:c8d99864ecd917ebbc3292f1a6b8cd38ce4ed882f38a0cf232d97c69ab2c9528", "2.8--pyh7cba7a3_0": "sha256:26545e5b845d1e5a94606ea392a47a8bce5c949d433de1ca3b7a6c56bbe5f66b", "2.9--pyh7cba7a3_0": "sha256:65467bc66e0f1f8a725b17198603e7260a58b9aa90dd0e565f4760f0c8b87d15", "2.10--pyhdfd78af_0": "sha256:8fce17975eb195a29b20709d0f39e64b77eeae0ba4e07ad853b8e733a1e00317", "2.11.1--pyhdfd78af_0": "sha256:9e2cbaa709d4abac95aa7876b5c7313fe4fe2b9e81735f6f770997a7c8c7e914", "2.12.1--pyhdfd78af_0": "sha256:2a2e58c7ae5a3aa909a8011270b227d48e8a954d6dd8aef43cfbb57ca1f743bf", "2.13.1--pyhdfd78af_0": "sha256:47a4f78725aa736d712bd1f0e7bd38de0bdc32daf942dace1e8bc1565c822a1e"}, "docker": "quay.io/biocontainers/nf-core", "aliases": {"cheetah": "/usr/local/bin/cheetah", "cheetah-analyze": "/usr/local/bin/cheetah-analyze", "cheetah-compile": "/usr/local/bin/cheetah-compile", "galaxy-tool-test": "/usr/local/bin/galaxy-tool-test", "import_igenome": "/usr/local/bin/import_igenome", "mulled-build": "/usr/local/bin/mulled-build", "mulled-build-channel": "/usr/local/bin/mulled-build-channel", "mulled-build-files": "/usr/local/bin/mulled-build-files", "mulled-build-tool": "/usr/local/bin/mulled-build-tool", "mulled-hash": "/usr/local/bin/mulled-hash", "mulled-list": "/usr/local/bin/mulled-list", "mulled-search": "/usr/local/bin/mulled-search", "mulled-update-singularity-containers": "/usr/local/bin/mulled-update-singularity-containers", "nf-core": "/usr/local/bin/nf-core", "refgenie": "/usr/local/bin/refgenie", "rich-click": "/usr/local/bin/rich-click", "scalar": "/usr/local/bin/scalar", "conda-env": "/usr/local/bin/conda-env", "cph": "/usr/local/bin/cph", "git": "/usr/local/bin/git", "git-cvsserver": "/usr/local/bin/git-cvsserver", "git-receive-pack": "/usr/local/bin/git-receive-pack", "git-shell": "/usr/local/bin/git-shell", "git-upload-archive": "/usr/local/bin/git-upload-archive", "git-upload-pack": "/usr/local/bin/git-upload-pack", "gitk": "/usr/local/bin/gitk", "docutils": "/usr/local/bin/docutils"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nf-core.
shpc-registry automated BioContainers addition for nf-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nf-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nf-core:2.13.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nf-core/2.13.1--pyhdfd78af_0
$ module help quay.io/biocontainers/nf-core/2.13.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nf-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nf-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nf-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nf-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nf-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nf-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cheetah

```bash
$ singularity exec <container> /usr/local/bin/cheetah
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-analyze

```bash
$ singularity exec <container> /usr/local/bin/cheetah-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cheetah-compile

```bash
$ singularity exec <container> /usr/local/bin/cheetah-compile
$ podman run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cheetah-compile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-tool-test

```bash
$ singularity exec <container> /usr/local/bin/galaxy-tool-test
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### import_igenome

```bash
$ singularity exec <container> /usr/local/bin/import_igenome
$ podman run --it --rm --entrypoint /usr/local/bin/import_igenome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_igenome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build

```bash
$ singularity exec <container> /usr/local/bin/mulled-build
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-channel

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-channel
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-files

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-files
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-tool

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-tool
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-hash

```bash
$ singularity exec <container> /usr/local/bin/mulled-hash
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-hash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-list

```bash
$ singularity exec <container> /usr/local/bin/mulled-list
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-search

```bash
$ singularity exec <container> /usr/local/bin/mulled-search
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-update-singularity-containers

```bash
$ singularity exec <container> /usr/local/bin/mulled-update-singularity-containers
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-update-singularity-containers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-core

```bash
$ singularity exec <container> /usr/local/bin/nf-core
$ podman run --it --rm --entrypoint /usr/local/bin/nf-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refgenie

```bash
$ singularity exec <container> /usr/local/bin/refgenie
$ podman run --it --rm --entrypoint /usr/local/bin/refgenie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refgenie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scalar

```bash
$ singularity exec <container> /usr/local/bin/scalar
$ podman run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda-env

```bash
$ singularity exec <container> /usr/local/bin/conda-env
$ podman run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git

```bash
$ singularity exec <container> /usr/local/bin/git
$ podman run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-cvsserver

```bash
$ singularity exec <container> /usr/local/bin/git-cvsserver
$ podman run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-cvsserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-receive-pack

```bash
$ singularity exec <container> /usr/local/bin/git-receive-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-receive-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-shell

```bash
$ singularity exec <container> /usr/local/bin/git-shell
$ podman run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-shell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-archive

```bash
$ singularity exec <container> /usr/local/bin/git-upload-archive
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-archive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-upload-pack

```bash
$ singularity exec <container> /usr/local/bin/git-upload-pack
$ podman run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-upload-pack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gitk

```bash
$ singularity exec <container> /usr/local/bin/gitk
$ podman run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gitk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
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