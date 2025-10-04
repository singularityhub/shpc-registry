---
layout: container
name:  "quay.io/biocontainers/perl-xml-libxml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-xml-libxml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-xml-libxml/container.yaml"
updated_at: "2025-10-04 03:07:30.810014"
latest: "2.0210--pl5321hd2ab53c_1"
container_url: "https://biocontainers.pro/tools/perl-xml-libxml"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.0207--pl5321h661654b_0"
 - "2.0210--pl5321hf886d80_0"
 - "2.0210--pl5321hd2ab53c_1"
description: "shpc-registry automated BioContainers addition for perl-xml-libxml"
config: {"url": "https://biocontainers.pro/tools/perl-xml-libxml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-xml-libxml", "latest": {"2.0210--pl5321hd2ab53c_1": "sha256:7aa965a8f1a65a1cce4e0920c4b98c7e783f86ea2894d2c2be0361d5afb7359b"}, "tags": {"2.0207--pl5321h661654b_0": "sha256:fc36314913ff96eeaeca42828bad93b839db0d86181e0801be8af8d27359b93a", "2.0210--pl5321hf886d80_0": "sha256:5385d7ba9398b53f8a90d87f54962069e7d6ec1a57527f21ef5ab6ed76322b0d", "2.0210--pl5321hd2ab53c_1": "sha256:7aa965a8f1a65a1cce4e0920c4b98c7e783f86ea2894d2c2be0361d5afb7359b"}, "docker": "quay.io/biocontainers/perl-xml-libxml", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-xml-libxml.
shpc-registry automated BioContainers addition for perl-xml-libxml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-xml-libxml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-xml-libxml:2.0210--pl5321hd2ab53c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-xml-libxml/2.0210--pl5321hd2ab53c_1
$ module help quay.io/biocontainers/perl-xml-libxml/2.0210--pl5321hd2ab53c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-xml-libxml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-xml-libxml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-xml-libxml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-xml-libxml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-xml-libxml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-xml-libxml-inspect-deffile:

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