---
layout: container
name:  "quay.io/biocontainers/bwakit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwakit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bwakit/container.yaml"
updated_at: "2022-10-29 05:39:34.717101"
latest: "0.7.17.dev1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bwakit"
aliases:
 - "bwa-postalt.js"
 - "fermi2"
 - "fermi2.pl"
 - "htsbox"
 - "ropebwt2"
 - "run-HLA"
 - "run-bwamem"
 - "run-gen-ref"
 - "samblaster"
 - "trimadap"
 - "typeHLA-selctg.js"
 - "typeHLA.js"
 - "typeHLA.sh"
 - "ace2sam"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "bwa"
 - "export2sam.pl"
 - "fasta-sanitize.pl"
 - "htsfile"
 - "interpolate_sam.pl"
 - "k8"
versions:
 - "0.7.17.dev1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bwakit"
config: {"url": "https://biocontainers.pro/tools/bwakit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bwakit", "latest": {"0.7.17.dev1--hdfd78af_1": "sha256:335464029b06a3726692c6cba1620c56b988f0dac202df3c3ae33ef9a2f434c4"}, "tags": {"0.7.17.dev1--hdfd78af_1": "sha256:335464029b06a3726692c6cba1620c56b988f0dac202df3c3ae33ef9a2f434c4"}, "docker": "quay.io/biocontainers/bwakit", "aliases": {"bwa-postalt.js": "/usr/local/bin/bwa-postalt.js", "fermi2": "/usr/local/bin/fermi2", "fermi2.pl": "/usr/local/bin/fermi2.pl", "htsbox": "/usr/local/bin/htsbox", "ropebwt2": "/usr/local/bin/ropebwt2", "run-HLA": "/usr/local/bin/run-HLA", "run-bwamem": "/usr/local/bin/run-bwamem", "run-gen-ref": "/usr/local/bin/run-gen-ref", "samblaster": "/usr/local/bin/samblaster", "trimadap": "/usr/local/bin/trimadap", "typeHLA-selctg.js": "/usr/local/bin/typeHLA-selctg.js", "typeHLA.js": "/usr/local/bin/typeHLA.js", "typeHLA.sh": "/usr/local/bin/typeHLA.sh", "ace2sam": "/usr/local/bin/ace2sam", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "bwa": "/usr/local/bin/bwa", "export2sam.pl": "/usr/local/bin/export2sam.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "htsfile": "/usr/local/bin/htsfile", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwakit.
shpc-registry automated BioContainers addition for bwakit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwakit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwakit:0.7.17.dev1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwakit/0.7.17.dev1--hdfd78af_1
$ module help quay.io/biocontainers/bwakit/0.7.17.dev1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwakit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwakit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwakit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwakit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwakit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwakit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa-postalt.js

```bash
$ singularity exec <container> /usr/local/bin/bwa-postalt.js
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-postalt.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-postalt.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2

```bash
$ singularity exec <container> /usr/local/bin/fermi2
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2.pl

```bash
$ singularity exec <container> /usr/local/bin/fermi2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsbox

```bash
$ singularity exec <container> /usr/local/bin/htsbox
$ podman run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ropebwt2

```bash
$ singularity exec <container> /usr/local/bin/ropebwt2
$ podman run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-HLA

```bash
$ singularity exec <container> /usr/local/bin/run-HLA
$ podman run --it --rm --entrypoint /usr/local/bin/run-HLA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-HLA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-bwamem

```bash
$ singularity exec <container> /usr/local/bin/run-bwamem
$ podman run --it --rm --entrypoint /usr/local/bin/run-bwamem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-bwamem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-gen-ref

```bash
$ singularity exec <container> /usr/local/bin/run-gen-ref
$ podman run --it --rm --entrypoint /usr/local/bin/run-gen-ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-gen-ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samblaster

```bash
$ singularity exec <container> /usr/local/bin/samblaster
$ podman run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimadap

```bash
$ singularity exec <container> /usr/local/bin/trimadap
$ podman run --it --rm --entrypoint /usr/local/bin/trimadap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimadap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typeHLA-selctg.js

```bash
$ singularity exec <container> /usr/local/bin/typeHLA-selctg.js
$ podman run --it --rm --entrypoint /usr/local/bin/typeHLA-selctg.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typeHLA-selctg.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typeHLA.js

```bash
$ singularity exec <container> /usr/local/bin/typeHLA.js
$ podman run --it --rm --entrypoint /usr/local/bin/typeHLA.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typeHLA.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typeHLA.sh

```bash
$ singularity exec <container> /usr/local/bin/typeHLA.sh
$ podman run --it --rm --entrypoint /usr/local/bin/typeHLA.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typeHLA.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl

```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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