---
layout: container
name:  "quay.io/biocontainers/metabinkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metabinkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metabinkit/container.yaml"
updated_at: "2024-10-16 03:29:57.186262"
latest: "0.2.3--r43h6ead514_2"
container_url: "https://biocontainers.pro/tools/metabinkit"
aliases:
 - "metabin"
 - "metabinkit_blast"
 - "metabinkit_blastgendb"
 - "metabinkit_shared.sh"
 - "taxonkit"
 - "taxonkit_children.sh"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "align-columns"
 - "blst2tkns"
 - "csv2xml"
 - "disambiguate-nucleotides"
versions:
 - "0.2.2--r41hbd632db_4"
 - "0.2.2--r42hbd632db_5"
 - "0.2.3--r42hbd632db_0"
 - "0.2.3--r42h6ead514_1"
 - "0.2.3--r43h6ead514_2"
description: "shpc-registry automated BioContainers addition for metabinkit"
config: {"url": "https://biocontainers.pro/tools/metabinkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metabinkit", "latest": {"0.2.3--r43h6ead514_2": "sha256:2e2a2e18586e0f6ced36bb793a6459a50751c2bbc6a4e6f1f180d1c0bdf8392c"}, "tags": {"0.2.2--r41hbd632db_4": "sha256:df0cb8a1995cb2badb2fcf5934bb0b6f5343c10cb167055b11230536204f3087", "0.2.2--r42hbd632db_5": "sha256:9dc6d509dddda59aa87f4f25a751d9ea789c4217f56996b49b25a560cff451bf", "0.2.3--r42hbd632db_0": "sha256:6ccb5b495f3792209103d95b3dcdeb3bd8987bf97e4627fc2867bcc6d7d5a6f0", "0.2.3--r42h6ead514_1": "sha256:d86c2d1f569e6acc33631283c2bfcc9268105cc6b0cbcbff42d0355b99279ac6", "0.2.3--r43h6ead514_2": "sha256:2e2a2e18586e0f6ced36bb793a6459a50751c2bbc6a4e6f1f180d1c0bdf8392c"}, "docker": "quay.io/biocontainers/metabinkit", "aliases": {"metabin": "/usr/local/bin/metabin", "metabinkit_blast": "/usr/local/bin/metabinkit_blast", "metabinkit_blastgendb": "/usr/local/bin/metabinkit_blastgendb", "metabinkit_shared.sh": "/usr/local/bin/metabinkit_shared.sh", "taxonkit": "/usr/local/bin/taxonkit", "taxonkit_children.sh": "/usr/local/bin/taxonkit_children.sh", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "align-columns": "/usr/local/bin/align-columns", "blst2tkns": "/usr/local/bin/blst2tkns", "csv2xml": "/usr/local/bin/csv2xml", "disambiguate-nucleotides": "/usr/local/bin/disambiguate-nucleotides"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metabinkit.
shpc-registry automated BioContainers addition for metabinkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metabinkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metabinkit:0.2.3--r43h6ead514_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metabinkit/0.2.3--r43h6ead514_2
$ module help quay.io/biocontainers/metabinkit/0.2.3--r43h6ead514_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metabinkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metabinkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metabinkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metabinkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metabinkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metabinkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metabin

```bash
$ singularity exec <container> /usr/local/bin/metabin
$ podman run --it --rm --entrypoint /usr/local/bin/metabin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabinkit_blast

```bash
$ singularity exec <container> /usr/local/bin/metabinkit_blast
$ podman run --it --rm --entrypoint /usr/local/bin/metabinkit_blast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabinkit_blast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabinkit_blastgendb

```bash
$ singularity exec <container> /usr/local/bin/metabinkit_blastgendb
$ podman run --it --rm --entrypoint /usr/local/bin/metabinkit_blastgendb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabinkit_blastgendb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabinkit_shared.sh

```bash
$ singularity exec <container> /usr/local/bin/metabinkit_shared.sh
$ podman run --it --rm --entrypoint /usr/local/bin/metabinkit_shared.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabinkit_shared.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit

```bash
$ singularity exec <container> /usr/local/bin/taxonkit
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxonkit_children.sh

```bash
$ singularity exec <container> /usr/local/bin/taxonkit_children.sh
$ podman run --it --rm --entrypoint /usr/local/bin/taxonkit_children.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxonkit_children.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blst2tkns

```bash
$ singularity exec <container> /usr/local/bin/blst2tkns
$ podman run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blst2tkns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2xml

```bash
$ singularity exec <container> /usr/local/bin/csv2xml
$ podman run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disambiguate-nucleotides

```bash
$ singularity exec <container> /usr/local/bin/disambiguate-nucleotides
$ podman run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disambiguate-nucleotides   -v ${PWD} -w ${PWD} <container> -c " $@"
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