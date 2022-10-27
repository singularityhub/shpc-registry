---
layout: container
name:  "quay.io/biocontainers/plant_tribes_gene_family_classifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plant_tribes_gene_family_classifier/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/plant_tribes_gene_family_classifier/container.yaml"
updated_at: "2022-10-27 00:53:33.897974"
latest: "1.0.4--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/plant_tribes_gene_family_classifier"
aliases:
 - "GeneFamilyClassifier"
versions:
 - "1.0.4--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for plant_tribes_gene_family_classifier"
config: {"url": "https://biocontainers.pro/tools/plant_tribes_gene_family_classifier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plant_tribes_gene_family_classifier", "latest": {"1.0.4--hdfd78af_2": "sha256:87b56a8ed527d2a08a2e733373a62b68502e17fdbb29adf7898cda601f284496"}, "tags": {"1.0.4--hdfd78af_2": "sha256:87b56a8ed527d2a08a2e733373a62b68502e17fdbb29adf7898cda601f284496"}, "docker": "quay.io/biocontainers/plant_tribes_gene_family_classifier", "aliases": {"GeneFamilyClassifier": "/usr/local/bin/GeneFamilyClassifier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plant_tribes_gene_family_classifier.
shpc-registry automated BioContainers addition for plant_tribes_gene_family_classifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_classifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plant_tribes_gene_family_classifier:1.0.4--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plant_tribes_gene_family_classifier/1.0.4--hdfd78af_2
$ module help quay.io/biocontainers/plant_tribes_gene_family_classifier/1.0.4--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plant_tribes_gene_family_classifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_classifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plant_tribes_gene_family_classifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plant_tribes_gene_family_classifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plant_tribes_gene_family_classifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plant_tribes_gene_family_classifier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeneFamilyClassifier

```bash
$ singularity exec <container> /usr/local/bin/GeneFamilyClassifier
$ podman run --it --rm --entrypoint /usr/local/bin/GeneFamilyClassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeneFamilyClassifier   -v ${PWD} -w ${PWD} <container> -c " $@"
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