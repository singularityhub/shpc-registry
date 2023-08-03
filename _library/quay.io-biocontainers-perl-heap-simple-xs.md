---
layout: container
name:  "quay.io/biocontainers/perl-heap-simple-xs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-heap-simple-xs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-heap-simple-xs/container.yaml"
updated_at: "2023-08-03 04:16:52.612161"
latest: "0.10--pl5321h031d066_6"
container_url: "https://biocontainers.pro/tools/perl-heap-simple-xs"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.10--pl5321hec16e2b_4"
 - "0.10--pl5321hec16e2b_5"
 - "0.10--pl5321h031d066_6"
description: "shpc-registry automated BioContainers addition for perl-heap-simple-xs"
config: {"url": "https://biocontainers.pro/tools/perl-heap-simple-xs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-heap-simple-xs", "latest": {"0.10--pl5321h031d066_6": "sha256:8cbd2d3bf112ad3e5fea02749cc6d793f36d617f7af9804a60bf40eb7cc16b66"}, "tags": {"0.10--pl5321hec16e2b_4": "sha256:3cd2ebbc9b5715b2c8ae033258ed692d11ffa0c6f2fe579a03861f8063a8c6f0", "0.10--pl5321hec16e2b_5": "sha256:7dedbf88dcf798d92896b74069ed4e2ef91d1ce816efdc9a19332e210a0c1366", "0.10--pl5321h031d066_6": "sha256:8cbd2d3bf112ad3e5fea02749cc6d793f36d617f7af9804a60bf40eb7cc16b66"}, "docker": "quay.io/biocontainers/perl-heap-simple-xs", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-heap-simple-xs.
shpc-registry automated BioContainers addition for perl-heap-simple-xs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-heap-simple-xs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-heap-simple-xs:0.10--pl5321h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-heap-simple-xs/0.10--pl5321h031d066_6
$ module help quay.io/biocontainers/perl-heap-simple-xs/0.10--pl5321h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-heap-simple-xs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-heap-simple-xs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-heap-simple-xs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-heap-simple-xs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-heap-simple-xs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-heap-simple-xs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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