---
layout: container
name:  "quay.io/biocontainers/mgkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mgkit/container.yaml"
updated_at: "2023-12-07 02:35:32.784558"
latest: "0.5.8--py39hf95cd2a_1"
container_url: "https://biocontainers.pro/tools/mgkit"
aliases:
 - "add-gff-info"
 - "blast2gff"
 - "download-ncbi-taxa.sh"
 - "download-taxonomy.sh"
 - "download-uniprot-taxa.sh"
 - "edit-gff"
 - "extract-gff-info"
 - "fasta-utils"
 - "fastq-utils"
 - "filter-gff"
 - "get-gff-info"
 - "hmmer2gff"
 - "htseq-count-barcodes"
 - "json2gff"
 - "pnps-gen"
 - "sampling-utils"
 - "snp_parser"
 - "sort-gff.sh"
 - "taxon-utils"
 - "htseq-count"
 - "htseq-qa"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "mirror_server"
 - "mirror_server_stop"
 - "f2py3.6"
 - "normalizer"
versions:
 - "0.5.6--py36h91eb985_1"
 - "0.5.8--py39hbf8eff0_0"
 - "0.5.8--py39hf95cd2a_1"
description: "shpc-registry automated BioContainers addition for mgkit"
config: {"url": "https://biocontainers.pro/tools/mgkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mgkit", "latest": {"0.5.8--py39hf95cd2a_1": "sha256:a54236bd3b43752338db429cdee724de71e14bfde65d3e0d61d6859b5974b37f"}, "tags": {"0.5.6--py36h91eb985_1": "sha256:48ba88f8625cb52ac37fcfe25caf643d4ffb29ef5998357b109a545cefc4a5fd", "0.5.8--py39hbf8eff0_0": "sha256:987920948efaab1690076606ad11f7390e160e49c1d48d4ff415ceb61f94e63e", "0.5.8--py39hf95cd2a_1": "sha256:a54236bd3b43752338db429cdee724de71e14bfde65d3e0d61d6859b5974b37f"}, "docker": "quay.io/biocontainers/mgkit", "aliases": {"add-gff-info": "/usr/local/bin/add-gff-info", "blast2gff": "/usr/local/bin/blast2gff", "download-ncbi-taxa.sh": "/usr/local/bin/download-ncbi-taxa.sh", "download-taxonomy.sh": "/usr/local/bin/download-taxonomy.sh", "download-uniprot-taxa.sh": "/usr/local/bin/download-uniprot-taxa.sh", "edit-gff": "/usr/local/bin/edit-gff", "extract-gff-info": "/usr/local/bin/extract-gff-info", "fasta-utils": "/usr/local/bin/fasta-utils", "fastq-utils": "/usr/local/bin/fastq-utils", "filter-gff": "/usr/local/bin/filter-gff", "get-gff-info": "/usr/local/bin/get-gff-info", "hmmer2gff": "/usr/local/bin/hmmer2gff", "htseq-count-barcodes": "/usr/local/bin/htseq-count-barcodes", "json2gff": "/usr/local/bin/json2gff", "pnps-gen": "/usr/local/bin/pnps-gen", "sampling-utils": "/usr/local/bin/sampling-utils", "snp_parser": "/usr/local/bin/snp_parser", "sort-gff.sh": "/usr/local/bin/sort-gff.sh", "taxon-utils": "/usr/local/bin/taxon-utils", "htseq-count": "/usr/local/bin/htseq-count", "htseq-qa": "/usr/local/bin/htseq-qa", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "f2py3.6": "/usr/local/bin/f2py3.6", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgkit.
shpc-registry automated BioContainers addition for mgkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgkit:0.5.8--py39hf95cd2a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgkit/0.5.8--py39hf95cd2a_1
$ module help quay.io/biocontainers/mgkit/0.5.8--py39hf95cd2a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add-gff-info

```bash
$ singularity exec <container> /usr/local/bin/add-gff-info
$ podman run --it --rm --entrypoint /usr/local/bin/add-gff-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add-gff-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2gff

```bash
$ singularity exec <container> /usr/local/bin/blast2gff
$ podman run --it --rm --entrypoint /usr/local/bin/blast2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-ncbi-taxa.sh

```bash
$ singularity exec <container> /usr/local/bin/download-ncbi-taxa.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-ncbi-taxa.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-ncbi-taxa.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-taxonomy.sh

```bash
$ singularity exec <container> /usr/local/bin/download-taxonomy.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-taxonomy.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-taxonomy.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-uniprot-taxa.sh

```bash
$ singularity exec <container> /usr/local/bin/download-uniprot-taxa.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-uniprot-taxa.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-uniprot-taxa.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edit-gff

```bash
$ singularity exec <container> /usr/local/bin/edit-gff
$ podman run --it --rm --entrypoint /usr/local/bin/edit-gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edit-gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract-gff-info

```bash
$ singularity exec <container> /usr/local/bin/extract-gff-info
$ podman run --it --rm --entrypoint /usr/local/bin/extract-gff-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-gff-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-utils

```bash
$ singularity exec <container> /usr/local/bin/fasta-utils
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-utils

```bash
$ singularity exec <container> /usr/local/bin/fastq-utils
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-gff

```bash
$ singularity exec <container> /usr/local/bin/filter-gff
$ podman run --it --rm --entrypoint /usr/local/bin/filter-gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get-gff-info

```bash
$ singularity exec <container> /usr/local/bin/get-gff-info
$ podman run --it --rm --entrypoint /usr/local/bin/get-gff-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-gff-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmer2gff

```bash
$ singularity exec <container> /usr/local/bin/hmmer2gff
$ podman run --it --rm --entrypoint /usr/local/bin/hmmer2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmer2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count-barcodes

```bash
$ singularity exec <container> /usr/local/bin/htseq-count-barcodes
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count-barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count-barcodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### json2gff

```bash
$ singularity exec <container> /usr/local/bin/json2gff
$ podman run --it --rm --entrypoint /usr/local/bin/json2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/json2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnps-gen

```bash
$ singularity exec <container> /usr/local/bin/pnps-gen
$ podman run --it --rm --entrypoint /usr/local/bin/pnps-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnps-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sampling-utils

```bash
$ singularity exec <container> /usr/local/bin/sampling-utils
$ podman run --it --rm --entrypoint /usr/local/bin/sampling-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sampling-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snp_parser

```bash
$ singularity exec <container> /usr/local/bin/snp_parser
$ podman run --it --rm --entrypoint /usr/local/bin/snp_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snp_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-gff.sh

```bash
$ singularity exec <container> /usr/local/bin/sort-gff.sh
$ podman run --it --rm --entrypoint /usr/local/bin/sort-gff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-gff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxon-utils

```bash
$ singularity exec <container> /usr/local/bin/taxon-utils
$ podman run --it --rm --entrypoint /usr/local/bin/taxon-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxon-utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-count

```bash
$ singularity exec <container> /usr/local/bin/htseq-count
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htseq-qa

```bash
$ singularity exec <container> /usr/local/bin/htseq-qa
$ podman run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htseq-qa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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