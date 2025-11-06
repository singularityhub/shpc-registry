---
layout: container
name:  "quay.io/biocontainers/fastaptamer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastaptamer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastaptamer/container.yaml"
updated_at: "2025-11-06 04:14:24.072186"
latest: "1.0.16--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/fastaptamer"
aliases:
 - "fastaptamer_cluster"
 - "fastaptamer_cluster_xs"
 - "fastaptamer_compare"
 - "fastaptamer_count"
 - "fastaptamer_enrich"
 - "fastaptamer_search"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "1.0.14--hdfd78af_1"
 - "1.0.16--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for fastaptamer"
config: {"url": "https://biocontainers.pro/tools/fastaptamer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastaptamer", "latest": {"1.0.16--hdfd78af_0": "sha256:a26858e2893400cc71ed9be5450e40b8dc26ad6b0bba6ac8f5e5123bbfe65707"}, "tags": {"1.0.14--hdfd78af_1": "sha256:835f80a358023c187eb0412452fe9884e3fef20d266981eab3f88d25c43456eb", "1.0.16--hdfd78af_0": "sha256:a26858e2893400cc71ed9be5450e40b8dc26ad6b0bba6ac8f5e5123bbfe65707"}, "docker": "quay.io/biocontainers/fastaptamer", "aliases": {"fastaptamer_cluster": "/usr/local/bin/fastaptamer_cluster", "fastaptamer_cluster_xs": "/usr/local/bin/fastaptamer_cluster_xs", "fastaptamer_compare": "/usr/local/bin/fastaptamer_compare", "fastaptamer_count": "/usr/local/bin/fastaptamer_count", "fastaptamer_enrich": "/usr/local/bin/fastaptamer_enrich", "fastaptamer_search": "/usr/local/bin/fastaptamer_search", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastaptamer.
shpc-registry automated BioContainers addition for fastaptamer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastaptamer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastaptamer:1.0.16--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastaptamer/1.0.16--hdfd78af_0
$ module help quay.io/biocontainers/fastaptamer/1.0.16--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastaptamer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastaptamer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastaptamer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastaptamer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastaptamer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastaptamer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastaptamer_cluster

```bash
$ singularity exec <container> /usr/local/bin/fastaptamer_cluster
$ podman run --it --rm --entrypoint /usr/local/bin/fastaptamer_cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaptamer_cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaptamer_cluster_xs

```bash
$ singularity exec <container> /usr/local/bin/fastaptamer_cluster_xs
$ podman run --it --rm --entrypoint /usr/local/bin/fastaptamer_cluster_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaptamer_cluster_xs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaptamer_compare

```bash
$ singularity exec <container> /usr/local/bin/fastaptamer_compare
$ podman run --it --rm --entrypoint /usr/local/bin/fastaptamer_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaptamer_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaptamer_count

```bash
$ singularity exec <container> /usr/local/bin/fastaptamer_count
$ podman run --it --rm --entrypoint /usr/local/bin/fastaptamer_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaptamer_count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaptamer_enrich

```bash
$ singularity exec <container> /usr/local/bin/fastaptamer_enrich
$ podman run --it --rm --entrypoint /usr/local/bin/fastaptamer_enrich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaptamer_enrich   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaptamer_search

```bash
$ singularity exec <container> /usr/local/bin/fastaptamer_search
$ podman run --it --rm --entrypoint /usr/local/bin/fastaptamer_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaptamer_search   -v ${PWD} -w ${PWD} <container> -c " $@"
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