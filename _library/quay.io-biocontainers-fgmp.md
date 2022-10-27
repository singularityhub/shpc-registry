---
layout: container
name:  "quay.io/biocontainers/fgmp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fgmp/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/fgmp/container.yaml"
updated_at: "2022-10-27 01:06:02.772896"
latest: "1.0.3--pl5321hdfd78af_3"
container_url: "https://biocontainers.pro/tools/fgmp"
aliases:
 - "PF00225_full.blocks.txt"
 - "PF00225_seed.blocks.txt"
 - "add_name_to_gff3.pl"
 - "aln2wig"
 - "augustify.py"
 - "esd2esi"
 - "executeTestCGP.py"
 - "exonerate"
 - "exonerate-server"
 - "extractAnno.py"
 - "fasta2esd"
 - "fastaannotatecdna"
 - "fastachecksum"
 - "fastaclip"
 - "fastacomposition"
 - "fastadiff"
 - "fastaexplode"
 - "fastafetch"
 - "fastahardmask"
 - "fastaindex"
 - "fastalength"
 - "fastanrdb"
 - "fastaoverlap"
 - "fastareformat"
 - "fastaremove"
 - "fastarevcomp"
 - "fastasoftmask"
 - "fastasort"
 - "fastasubseq"
 - "fastatranslate"
 - "fastavalidcds"
 - "fgmp"
 - "get_loci_from_gb.pl"
 - "ipcress"
 - "pp_simScore"
versions:
 - "1.0.3--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for fgmp"
config: {"url": "https://biocontainers.pro/tools/fgmp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fgmp", "latest": {"1.0.3--pl5321hdfd78af_3": "sha256:203b2388b9d8db44104ccbe9f1d07a8e8ce52e755242196891e4a82c12c746ea"}, "tags": {"1.0.3--pl5321hdfd78af_3": "sha256:203b2388b9d8db44104ccbe9f1d07a8e8ce52e755242196891e4a82c12c746ea"}, "docker": "quay.io/biocontainers/fgmp", "aliases": {"PF00225_full.blocks.txt": "/usr/local/bin/PF00225_full.blocks.txt", "PF00225_seed.blocks.txt": "/usr/local/bin/PF00225_seed.blocks.txt", "add_name_to_gff3.pl": "/usr/local/bin/add_name_to_gff3.pl", "aln2wig": "/usr/local/bin/aln2wig", "augustify.py": "/usr/local/bin/augustify.py", "esd2esi": "/usr/local/bin/esd2esi", "executeTestCGP.py": "/usr/local/bin/executeTestCGP.py", "exonerate": "/usr/local/bin/exonerate", "exonerate-server": "/usr/local/bin/exonerate-server", "extractAnno.py": "/usr/local/bin/extractAnno.py", "fasta2esd": "/usr/local/bin/fasta2esd", "fastaannotatecdna": "/usr/local/bin/fastaannotatecdna", "fastachecksum": "/usr/local/bin/fastachecksum", "fastaclip": "/usr/local/bin/fastaclip", "fastacomposition": "/usr/local/bin/fastacomposition", "fastadiff": "/usr/local/bin/fastadiff", "fastaexplode": "/usr/local/bin/fastaexplode", "fastafetch": "/usr/local/bin/fastafetch", "fastahardmask": "/usr/local/bin/fastahardmask", "fastaindex": "/usr/local/bin/fastaindex", "fastalength": "/usr/local/bin/fastalength", "fastanrdb": "/usr/local/bin/fastanrdb", "fastaoverlap": "/usr/local/bin/fastaoverlap", "fastareformat": "/usr/local/bin/fastareformat", "fastaremove": "/usr/local/bin/fastaremove", "fastarevcomp": "/usr/local/bin/fastarevcomp", "fastasoftmask": "/usr/local/bin/fastasoftmask", "fastasort": "/usr/local/bin/fastasort", "fastasubseq": "/usr/local/bin/fastasubseq", "fastatranslate": "/usr/local/bin/fastatranslate", "fastavalidcds": "/usr/local/bin/fastavalidcds", "fgmp": "/usr/local/bin/fgmp", "get_loci_from_gb.pl": "/usr/local/bin/get_loci_from_gb.pl", "ipcress": "/usr/local/bin/ipcress", "pp_simScore": "/usr/local/bin/pp_simScore"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fgmp.
shpc-registry automated BioContainers addition for fgmp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fgmp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fgmp:1.0.3--pl5321hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fgmp/1.0.3--pl5321hdfd78af_3
$ module help quay.io/biocontainers/fgmp/1.0.3--pl5321hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fgmp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fgmp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fgmp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fgmp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fgmp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fgmp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PF00225_full.blocks.txt

```bash
$ singularity exec <container> /usr/local/bin/PF00225_full.blocks.txt
$ podman run --it --rm --entrypoint /usr/local/bin/PF00225_full.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PF00225_full.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PF00225_seed.blocks.txt

```bash
$ singularity exec <container> /usr/local/bin/PF00225_seed.blocks.txt
$ podman run --it --rm --entrypoint /usr/local/bin/PF00225_seed.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PF00225_seed.blocks.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### add_name_to_gff3.pl

```bash
$ singularity exec <container> /usr/local/bin/add_name_to_gff3.pl
$ podman run --it --rm --entrypoint /usr/local/bin/add_name_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_name_to_gff3.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aln2wig

```bash
$ singularity exec <container> /usr/local/bin/aln2wig
$ podman run --it --rm --entrypoint /usr/local/bin/aln2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aln2wig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### augustify.py

```bash
$ singularity exec <container> /usr/local/bin/augustify.py
$ podman run --it --rm --entrypoint /usr/local/bin/augustify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/augustify.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esd2esi

```bash
$ singularity exec <container> /usr/local/bin/esd2esi
$ podman run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### executeTestCGP.py

```bash
$ singularity exec <container> /usr/local/bin/executeTestCGP.py
$ podman run --it --rm --entrypoint /usr/local/bin/executeTestCGP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/executeTestCGP.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate

```bash
$ singularity exec <container> /usr/local/bin/exonerate
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate-server

```bash
$ singularity exec <container> /usr/local/bin/exonerate-server
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extractAnno.py

```bash
$ singularity exec <container> /usr/local/bin/extractAnno.py
$ podman run --it --rm --entrypoint /usr/local/bin/extractAnno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extractAnno.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2esd

```bash
$ singularity exec <container> /usr/local/bin/fasta2esd
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaannotatecdna

```bash
$ singularity exec <container> /usr/local/bin/fastaannotatecdna
$ podman run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastachecksum

```bash
$ singularity exec <container> /usr/local/bin/fastachecksum
$ podman run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaclip

```bash
$ singularity exec <container> /usr/local/bin/fastaclip
$ podman run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacomposition

```bash
$ singularity exec <container> /usr/local/bin/fastacomposition
$ podman run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastadiff

```bash
$ singularity exec <container> /usr/local/bin/fastadiff
$ podman run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaexplode

```bash
$ singularity exec <container> /usr/local/bin/fastaexplode
$ podman run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastafetch

```bash
$ singularity exec <container> /usr/local/bin/fastafetch
$ podman run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastahardmask

```bash
$ singularity exec <container> /usr/local/bin/fastahardmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaindex

```bash
$ singularity exec <container> /usr/local/bin/fastaindex
$ podman run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastalength

```bash
$ singularity exec <container> /usr/local/bin/fastalength
$ podman run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastanrdb

```bash
$ singularity exec <container> /usr/local/bin/fastanrdb
$ podman run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaoverlap

```bash
$ singularity exec <container> /usr/local/bin/fastaoverlap
$ podman run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastareformat

```bash
$ singularity exec <container> /usr/local/bin/fastareformat
$ podman run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaremove

```bash
$ singularity exec <container> /usr/local/bin/fastaremove
$ podman run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastarevcomp

```bash
$ singularity exec <container> /usr/local/bin/fastarevcomp
$ podman run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasoftmask

```bash
$ singularity exec <container> /usr/local/bin/fastasoftmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasort

```bash
$ singularity exec <container> /usr/local/bin/fastasort
$ podman run --it --rm --entrypoint /usr/local/bin/fastasort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasubseq

```bash
$ singularity exec <container> /usr/local/bin/fastasubseq
$ podman run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastatranslate

```bash
$ singularity exec <container> /usr/local/bin/fastatranslate
$ podman run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastavalidcds

```bash
$ singularity exec <container> /usr/local/bin/fastavalidcds
$ podman run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgmp

```bash
$ singularity exec <container> /usr/local/bin/fgmp
$ podman run --it --rm --entrypoint /usr/local/bin/fgmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_loci_from_gb.pl

```bash
$ singularity exec <container> /usr/local/bin/get_loci_from_gb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_loci_from_gb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcress

```bash
$ singularity exec <container> /usr/local/bin/ipcress
$ podman run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pp_simScore

```bash
$ singularity exec <container> /usr/local/bin/pp_simScore
$ podman run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pp_simScore   -v ${PWD} -w ${PWD} <container> -c " $@"
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