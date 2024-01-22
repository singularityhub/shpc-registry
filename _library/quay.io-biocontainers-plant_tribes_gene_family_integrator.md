---
layout: container
name:  "quay.io/biocontainers/plant_tribes_gene_family_integrator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plant_tribes_gene_family_integrator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plant_tribes_gene_family_integrator/container.yaml"
updated_at: "2024-01-22 03:07:22.014829"
latest: "1.0.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/plant_tribes_gene_family_integrator"
aliases:
 - "GeneFamilyIntegrator"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "1.0.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for plant_tribes_gene_family_integrator"
config: {"url": "https://biocontainers.pro/tools/plant_tribes_gene_family_integrator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plant_tribes_gene_family_integrator", "latest": {"1.0.4--hdfd78af_1": "sha256:85ed2e8f6e722ba912b1760df544aa29916e8a83ed3e98e2f36e2fbcc0cfcceb"}, "tags": {"1.0.4--hdfd78af_1": "sha256:85ed2e8f6e722ba912b1760df544aa29916e8a83ed3e98e2f36e2fbcc0cfcceb"}, "docker": "quay.io/biocontainers/plant_tribes_gene_family_integrator", "aliases": {"GeneFamilyIntegrator": "/usr/local/bin/GeneFamilyIntegrator", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plant_tribes_gene_family_integrator.
shpc-registry automated BioContainers addition for plant_tribes_gene_family_integrator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_integrator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_integrator:1.0.4--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plant_tribes_gene_family_integrator/1.0.4--hdfd78af_1
$ module help quay.io/biocontainers/plant_tribes_gene_family_integrator/1.0.4--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plant_tribes_gene_family_integrator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_integrator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_integrator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plant_tribes_gene_family_integrator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plant_tribes_gene_family_integrator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plant_tribes_gene_family_integrator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeneFamilyIntegrator

```bash
$ singularity exec <container> /usr/local/bin/GeneFamilyIntegrator
$ podman run --it --rm --entrypoint /usr/local/bin/GeneFamilyIntegrator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneFamilyIntegrator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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