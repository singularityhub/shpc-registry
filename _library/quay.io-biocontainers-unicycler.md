---
layout: container
name:  "quay.io/biocontainers/unicycler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unicycler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unicycler/container.yaml"
updated_at: "2026-02-07 04:45:15.065748"
latest: "0.5.1--py312hdcc493e_5"
container_url: "https://biocontainers.pro/tools/unicycler"
aliases:
 - "coronaspades.py"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "miniasm"
 - "minidot"
 - "rnaviralspades.py"
 - "unicycler"
 - "racon"
 - "rampler"
 - "racon_wrapper"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "mag-improve"
 - "spades-convert-bin-to-fasta"
 - "spades-gsimplifier"
 - "spades-kmer-estimating"
 - "spades-read-filter"
versions:
 - "0.5.0--py39h2add14b_2"
 - "0.5.0--py310h6cc9453_3"
 - "0.5.0--py38h5cf8b27_3"
 - "0.5.0--py39heaaa4ec_5"
 - "0.5.1--py312hc60241a_1"
 - "0.5.1--py310hdf79db3_2"
 - "0.5.1--py311hc84137b_3"
 - "0.5.1--py311hc84137b_4"
 - "0.5.1--py312hdcc493e_5"
description: "shpc-registry automated BioContainers addition for unicycler"
config: {"url": "https://biocontainers.pro/tools/unicycler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unicycler", "latest": {"0.5.1--py312hdcc493e_5": "sha256:b25dfde145eeb8cc82f8f48c44f407e2ce6d41db42908451306dba1bdd22a3af"}, "tags": {"0.5.0--py39h2add14b_2": "sha256:d495c3c71c7a8f1d61da9ac48d114ba6e2bcd17c62f4c5a580d29bc643ddd4da", "0.5.0--py310h6cc9453_3": "sha256:c26377b76e34aca17fb6165b46593525a38e57265f659d11635ded110358a9dc", "0.5.0--py38h5cf8b27_3": "sha256:7832bd275b3e2c1f68d55b04e354ed63ded75206ef8e69ea6437b2d7551bfd3e", "0.5.0--py39heaaa4ec_5": "sha256:71d0072e8de90d218adce2fd6908d195f6f811ba5e0ceef56b865fc497e592c6", "0.5.1--py312hc60241a_1": "sha256:06574951acb41e02ffce013ee9d46ef4303e6f8ff49ac40ed8ddf4898414a7d6", "0.5.1--py310hdf79db3_2": "sha256:cc738c37c9f6d58825447b935282c51a7d634e249a90cd5a700aa93d5cc3b826", "0.5.1--py311hc84137b_3": "sha256:d289db000352af8504dc1dfb646170d1881a4b1cbb0e8d2e8522e90fef89fafc", "0.5.1--py311hc84137b_4": "sha256:742bc4e4fef3ce67836603a612f114135fc53a67b86def173ca26cbc51b9e8bb", "0.5.1--py312hdcc493e_5": "sha256:b25dfde145eeb8cc82f8f48c44f407e2ce6d41db42908451306dba1bdd22a3af"}, "docker": "quay.io/biocontainers/unicycler", "aliases": {"coronaspades.py": "/usr/local/bin/coronaspades.py", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "miniasm": "/usr/local/bin/miniasm", "minidot": "/usr/local/bin/minidot", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "unicycler": "/usr/local/bin/unicycler", "racon": "/usr/local/bin/racon", "rampler": "/usr/local/bin/rampler", "racon_wrapper": "/usr/local/bin/racon_wrapper", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "mag-improve": "/usr/local/bin/mag-improve", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-read-filter": "/usr/local/bin/spades-read-filter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unicycler.
shpc-registry automated BioContainers addition for unicycler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unicycler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unicycler:0.5.1--py312hdcc493e_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unicycler/0.5.1--py312hdcc493e_5
$ module help quay.io/biocontainers/unicycler/0.5.1--py312hdcc493e_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unicycler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unicycler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unicycler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unicycler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unicycler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unicycler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaplasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### miniasm

```bash
$ singularity exec <container> /usr/local/bin/miniasm
$ podman run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minidot

```bash
$ singularity exec <container> /usr/local/bin/minidot
$ podman run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler

```bash
$ singularity exec <container> /usr/local/bin/unicycler
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rampler

```bash
$ singularity exec <container> /usr/local/bin/rampler
$ podman run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon_wrapper

```bash
$ singularity exec <container> /usr/local/bin/racon_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-mapping-stats

```bash
$ singularity exec <container> /usr/local/bin/cds-mapping-stats
$ podman run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-subgraphs

```bash
$ singularity exec <container> /usr/local/bin/cds-subgraphs
$ podman run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mag-improve

```bash
$ singularity exec <container> /usr/local/bin/mag-improve
$ podman run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gsimplifier

```bash
$ singularity exec <container> /usr/local/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmer-estimating

```bash
$ singularity exec <container> /usr/local/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter

```bash
$ singularity exec <container> /usr/local/bin/spades-read-filter
$ podman run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
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