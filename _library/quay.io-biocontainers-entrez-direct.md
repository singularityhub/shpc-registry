---
layout: container
name:  "quay.io/biocontainers/entrez-direct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/entrez-direct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/entrez-direct/container.yaml"
updated_at: "2024-12-07 02:17:48.265488"
latest: "22.4--he881be0_0"
container_url: "https://biocontainers.pro/tools/entrez-direct"
aliases:
 - "asp-ls.bak"
 - "edirect.pl.bak"
 - "edirutil.bak"
 - "erase-pubmed"
 - "ftp-cp.bak"
 - "ftp-ls.bak"
 - "gbf2xml.bak"
 - "get-stash-uids"
 - "invert-pubmed"
 - "log-pubmed"
 - "master-pubmed"
 - "merge-pubmed"
 - "nquire.bak"
 - "prepare-stash"
 - "promote-pubmed"
 - "refresh-versioned"
 - "repack-pubmed"
 - "run-ncbi-converter.bak"
 - "setup-deps.pl.bak"
 - "setup.sh.orig"
 - "stash-pubmed"
 - "common.go"
 - "rchive.go"
 - "setup-deps.log"
 - "setup.sh"
 - "xtract.go"
 - "asp-cp"
 - "asp-ls"
 - "has-asp"
 - "index-pubmed"
 - "eaddress"
versions:
 - "7.70--pl526_2"
 - "16.2--he881be0_1"
 - "15.6--he881be0_1"
 - "13.9--pl5262he881be0_2"
 - "13.8--pl526h375a9b1_0"
 - "13.3--pl526h375a9b1_0"
 - "21.6--he881be0_0"
 - "22.1--he881be0_0"
 - "22.4--he881be0_0"
description: "shpc-registry automated BioContainers addition for entrez-direct"
config: {"url": "https://biocontainers.pro/tools/entrez-direct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for entrez-direct", "latest": {"22.4--he881be0_0": "sha256:07d6f38091457055aa9f93479fddb3a939eb703fc54445778521ae0b60966e6b"}, "tags": {"7.70--pl526_2": "sha256:d48a7270674f40ab3615fbb01533dc1d059f78c73549b2c08eebd0e8fa663ee6", "16.2--he881be0_1": "sha256:08a155e41ff29d396620a40906a16d3285fa21b508704ea161aeb3c2e071ef07", "15.6--he881be0_1": "sha256:35b05f61e8a0e6c208f282b282b4834b739dd439f20671df1623ed5bc1c7b8c6", "13.9--pl5262he881be0_2": "sha256:c8d5868f25ae6d0ff2389cec69c618f6f49d8b836e1786f9e49cff0bc21dbede", "13.8--pl526h375a9b1_0": "sha256:bb569f53c1a9f96228df380810945df1da91c7cc68048f6ae4d3a650e79a838c", "13.3--pl526h375a9b1_0": "sha256:861091e023c59e6b5d39e54954ad284c31ed684dc7530aa1431ca6047c161c5f", "21.6--he881be0_0": "sha256:2306b887474eaeae13f3932b00a37f8acf4babf17008e028be6e90ed872a89b9", "22.1--he881be0_0": "sha256:73bbc354c23db556ee44f1f5b486c8314366ff2cf08497eb56b71bd26a38b280", "22.4--he881be0_0": "sha256:07d6f38091457055aa9f93479fddb3a939eb703fc54445778521ae0b60966e6b"}, "docker": "quay.io/biocontainers/entrez-direct", "aliases": {"asp-ls.bak": "/usr/local/bin/asp-ls.bak", "edirect.pl.bak": "/usr/local/bin/edirect.pl.bak", "edirutil.bak": "/usr/local/bin/edirutil.bak", "erase-pubmed": "/usr/local/bin/erase-pubmed", "ftp-cp.bak": "/usr/local/bin/ftp-cp.bak", "ftp-ls.bak": "/usr/local/bin/ftp-ls.bak", "gbf2xml.bak": "/usr/local/bin/gbf2xml.bak", "get-stash-uids": "/usr/local/bin/get-stash-uids", "invert-pubmed": "/usr/local/bin/invert-pubmed", "log-pubmed": "/usr/local/bin/log-pubmed", "master-pubmed": "/usr/local/bin/master-pubmed", "merge-pubmed": "/usr/local/bin/merge-pubmed", "nquire.bak": "/usr/local/bin/nquire.bak", "prepare-stash": "/usr/local/bin/prepare-stash", "promote-pubmed": "/usr/local/bin/promote-pubmed", "refresh-versioned": "/usr/local/bin/refresh-versioned", "repack-pubmed": "/usr/local/bin/repack-pubmed", "run-ncbi-converter.bak": "/usr/local/bin/run-ncbi-converter.bak", "setup-deps.pl.bak": "/usr/local/bin/setup-deps.pl.bak", "setup.sh.orig": "/usr/local/bin/setup.sh.orig", "stash-pubmed": "/usr/local/bin/stash-pubmed", "common.go": "/usr/local/bin/common.go", "rchive.go": "/usr/local/bin/rchive.go", "setup-deps.log": "/usr/local/bin/setup-deps.log", "setup.sh": "/usr/local/bin/setup.sh", "xtract.go": "/usr/local/bin/xtract.go", "asp-cp": "/usr/local/bin/asp-cp", "asp-ls": "/usr/local/bin/asp-ls", "has-asp": "/usr/local/bin/has-asp", "index-pubmed": "/usr/local/bin/index-pubmed", "eaddress": "/usr/local/bin/eaddress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/entrez-direct.
shpc-registry automated BioContainers addition for entrez-direct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/entrez-direct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/entrez-direct:22.4--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/entrez-direct/22.4--he881be0_0
$ module help quay.io/biocontainers/entrez-direct/22.4--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### entrez-direct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### entrez-direct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### entrez-direct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### entrez-direct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### entrez-direct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### entrez-direct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asp-ls.bak

```bash
$ singularity exec <container> /usr/local/bin/asp-ls.bak
$ podman run --it --rm --entrypoint /usr/local/bin/asp-ls.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-ls.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/edirect.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirutil.bak

```bash
$ singularity exec <container> /usr/local/bin/edirutil.bak
$ podman run --it --rm --entrypoint /usr/local/bin/edirutil.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirutil.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erase-pubmed

```bash
$ singularity exec <container> /usr/local/bin/erase-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/erase-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/erase-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftp-cp.bak

```bash
$ singularity exec <container> /usr/local/bin/ftp-cp.bak
$ podman run --it --rm --entrypoint /usr/local/bin/ftp-cp.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftp-cp.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ftp-ls.bak

```bash
$ singularity exec <container> /usr/local/bin/ftp-ls.bak
$ podman run --it --rm --entrypoint /usr/local/bin/ftp-ls.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ftp-ls.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2xml.bak

```bash
$ singularity exec <container> /usr/local/bin/gbf2xml.bak
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2xml.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2xml.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-stash-uids

```bash
$ singularity exec <container> /usr/local/bin/get-stash-uids
$ podman run --it --rm --entrypoint /usr/local/bin/get-stash-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-stash-uids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### invert-pubmed

```bash
$ singularity exec <container> /usr/local/bin/invert-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/invert-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/invert-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### log-pubmed

```bash
$ singularity exec <container> /usr/local/bin/log-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/log-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/log-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### master-pubmed

```bash
$ singularity exec <container> /usr/local/bin/master-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/master-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/master-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-pubmed

```bash
$ singularity exec <container> /usr/local/bin/merge-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/merge-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nquire.bak

```bash
$ singularity exec <container> /usr/local/bin/nquire.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nquire.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nquire.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare-stash

```bash
$ singularity exec <container> /usr/local/bin/prepare-stash
$ podman run --it --rm --entrypoint /usr/local/bin/prepare-stash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare-stash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promote-pubmed

```bash
$ singularity exec <container> /usr/local/bin/promote-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/promote-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promote-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refresh-versioned

```bash
$ singularity exec <container> /usr/local/bin/refresh-versioned
$ podman run --it --rm --entrypoint /usr/local/bin/refresh-versioned   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refresh-versioned   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repack-pubmed

```bash
$ singularity exec <container> /usr/local/bin/repack-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/repack-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repack-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-ncbi-converter.bak

```bash
$ singularity exec <container> /usr/local/bin/run-ncbi-converter.bak
$ podman run --it --rm --entrypoint /usr/local/bin/run-ncbi-converter.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-ncbi-converter.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup-deps.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/setup-deps.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/setup-deps.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup-deps.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.sh.orig

```bash
$ singularity exec <container> /usr/local/bin/setup.sh.orig
$ podman run --it --rm --entrypoint /usr/local/bin/setup.sh.orig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.sh.orig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stash-pubmed

```bash
$ singularity exec <container> /usr/local/bin/stash-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/stash-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stash-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### common.go

```bash
$ singularity exec <container> /usr/local/bin/common.go
$ podman run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/common.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rchive.go

```bash
$ singularity exec <container> /usr/local/bin/rchive.go
$ podman run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rchive.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup-deps.log

```bash
$ singularity exec <container> /usr/local/bin/setup-deps.log
$ podman run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup-deps.log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setup.sh

```bash
$ singularity exec <container> /usr/local/bin/setup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xtract.go

```bash
$ singularity exec <container> /usr/local/bin/xtract.go
$ podman run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xtract.go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-cp

```bash
$ singularity exec <container> /usr/local/bin/asp-cp
$ podman run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asp-ls

```bash
$ singularity exec <container> /usr/local/bin/asp-ls
$ podman run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asp-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### has-asp

```bash
$ singularity exec <container> /usr/local/bin/has-asp
$ podman run --it --rm --entrypoint /usr/local/bin/has-asp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/has-asp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-pubmed

```bash
$ singularity exec <container> /usr/local/bin/index-pubmed
$ podman run --it --rm --entrypoint /usr/local/bin/index-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-pubmed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eaddress

```bash
$ singularity exec <container> /usr/local/bin/eaddress
$ podman run --it --rm --entrypoint /usr/local/bin/eaddress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eaddress   -v ${PWD} -w ${PWD} <container> -c " $@"
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