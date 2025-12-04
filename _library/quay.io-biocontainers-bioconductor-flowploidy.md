---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowploidy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowploidy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowploidy/container.yaml"
updated_at: "2025-12-04 04:12:26.515228"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowploidy"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowploidy"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowploidy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowploidy", "latest": {"1.32.0--r44hdfd78af_0": "sha256:543cbafe5a26614cc49960d8287fdfbd43ed3f5d7e8bab918858eae6d92efdb8"}, "tags": {"1.8.0--r351_0": "sha256:eb1607a48cfe5049ee19c53e1bc98df88372ac093c18197327b5a06694c79823", "1.24.0--r42hdfd78af_0": "sha256:c13e505924b959fb59ae0b06e7ea3108161b2efd563f30dd24d79f8036fef71b", "1.20.0--r41hdfd78af_0": "sha256:0130639bdb56f74179ed32a9d5c877d11b4d81e2c3464a741bc512bd7d29e246", "1.18.0--r41hdfd78af_0": "sha256:5b4d50f2f68b3870791bdeb532c90f25f2deebb741dcbf71a317372fe2f722e4", "1.16.0--r40hdfd78af_1": "sha256:f148e9be17b60314fe2565e9d3ee633aa315bdd838e93347ac26da2440634cbf", "1.14.0--r40_0": "sha256:178dc4ffad4384030064d738a05bf5de25ca360fc3c2e143f3cc721723e230c4", "1.26.0--r43hdfd78af_0": "sha256:c3a6e489889f2f7b943b37d462dc12edd5a2ea526e9bbd77ca926ea4406e2a77", "1.28.0--r43hdfd78af_0": "sha256:642f539d2b1adecafc97953bd6df6a8b83baa244428352589b12f1e6f673089c", "1.32.0--r44hdfd78af_0": "sha256:543cbafe5a26614cc49960d8287fdfbd43ed3f5d7e8bab918858eae6d92efdb8"}, "docker": "quay.io/biocontainers/bioconductor-flowploidy", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowploidy.
shpc-registry automated BioContainers addition for bioconductor-flowploidy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowploidy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowploidy:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowploidy/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowploidy/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowploidy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowploidy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowploidy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowploidy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowploidy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowploidy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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