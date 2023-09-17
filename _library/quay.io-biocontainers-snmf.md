---
layout: container
name:  "quay.io/biocontainers/snmf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snmf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snmf/container.yaml"
updated_at: "2023-09-17 00:21:59.063224"
latest: "1.2--pl526h516909a_2"
container_url: "https://biocontainers.pro/tools/snmf"
aliases:
 - "ancestrymap2geno"
 - "createDataSet"
 - "crossEntropy"
 - "geno2lfmm"
 - "lfmm2geno"
 - "ped2geno"
 - "sNMF"
 - "vcf2geno"
 - "bp_pairwise_kaks.pl"
 - "bp_search2BSML.pl"
 - "bp_aacomp.pl"
 - "bp_biofetch_genbank_proxy.pl"
 - "bp_bioflat_index.pl"
 - "bp_biogetseq.pl"
 - "bp_blast2tree.pl"
 - "bp_bulk_load_gff.pl"
 - "bp_chaos_plot.pl"
 - "bp_classify_hits_kingdom.pl"
versions:
 - "1.2--pl526h516909a_2"
description: "shpc-registry automated BioContainers addition for snmf"
config: {"url": "https://biocontainers.pro/tools/snmf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snmf", "latest": {"1.2--pl526h516909a_2": "sha256:70d792ac2bfd3c00a6fc3eb575d0ab3efa674b1eefc38dbfe59f188336b662ad"}, "tags": {"1.2--pl526h516909a_2": "sha256:70d792ac2bfd3c00a6fc3eb575d0ab3efa674b1eefc38dbfe59f188336b662ad"}, "docker": "quay.io/biocontainers/snmf", "aliases": {"ancestrymap2geno": "/usr/local/bin/ancestrymap2geno", "createDataSet": "/usr/local/bin/createDataSet", "crossEntropy": "/usr/local/bin/crossEntropy", "geno2lfmm": "/usr/local/bin/geno2lfmm", "lfmm2geno": "/usr/local/bin/lfmm2geno", "ped2geno": "/usr/local/bin/ped2geno", "sNMF": "/usr/local/bin/sNMF", "vcf2geno": "/usr/local/bin/vcf2geno", "bp_pairwise_kaks.pl": "/usr/local/bin/bp_pairwise_kaks.pl", "bp_search2BSML.pl": "/usr/local/bin/bp_search2BSML.pl", "bp_aacomp.pl": "/usr/local/bin/bp_aacomp.pl", "bp_biofetch_genbank_proxy.pl": "/usr/local/bin/bp_biofetch_genbank_proxy.pl", "bp_bioflat_index.pl": "/usr/local/bin/bp_bioflat_index.pl", "bp_biogetseq.pl": "/usr/local/bin/bp_biogetseq.pl", "bp_blast2tree.pl": "/usr/local/bin/bp_blast2tree.pl", "bp_bulk_load_gff.pl": "/usr/local/bin/bp_bulk_load_gff.pl", "bp_chaos_plot.pl": "/usr/local/bin/bp_chaos_plot.pl", "bp_classify_hits_kingdom.pl": "/usr/local/bin/bp_classify_hits_kingdom.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snmf.
shpc-registry automated BioContainers addition for snmf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snmf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snmf:1.2--pl526h516909a_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snmf/1.2--pl526h516909a_2
$ module help quay.io/biocontainers/snmf/1.2--pl526h516909a_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snmf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snmf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snmf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snmf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snmf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snmf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ancestrymap2geno

```bash
$ singularity exec <container> /usr/local/bin/ancestrymap2geno
$ podman run --it --rm --entrypoint /usr/local/bin/ancestrymap2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ancestrymap2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createDataSet

```bash
$ singularity exec <container> /usr/local/bin/createDataSet
$ podman run --it --rm --entrypoint /usr/local/bin/createDataSet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/createDataSet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crossEntropy

```bash
$ singularity exec <container> /usr/local/bin/crossEntropy
$ podman run --it --rm --entrypoint /usr/local/bin/crossEntropy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crossEntropy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geno2lfmm

```bash
$ singularity exec <container> /usr/local/bin/geno2lfmm
$ podman run --it --rm --entrypoint /usr/local/bin/geno2lfmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geno2lfmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lfmm2geno

```bash
$ singularity exec <container> /usr/local/bin/lfmm2geno
$ podman run --it --rm --entrypoint /usr/local/bin/lfmm2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lfmm2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ped2geno

```bash
$ singularity exec <container> /usr/local/bin/ped2geno
$ podman run --it --rm --entrypoint /usr/local/bin/ped2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ped2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sNMF

```bash
$ singularity exec <container> /usr/local/bin/sNMF
$ podman run --it --rm --entrypoint /usr/local/bin/sNMF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sNMF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2geno

```bash
$ singularity exec <container> /usr/local/bin/vcf2geno
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2geno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_pairwise_kaks.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_pairwise_kaks.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_pairwise_kaks.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_search2BSML.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_search2BSML.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_search2BSML.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biofetch_genbank_proxy.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biofetch_genbank_proxy.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biofetch_genbank_proxy.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_biogetseq.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_biogetseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_biogetseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_blast2tree.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_blast2tree.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_blast2tree.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bulk_load_gff.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_bulk_load_gff.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bulk_load_gff.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_chaos_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_chaos_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_chaos_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_classify_hits_kingdom.pl

```bash
$ singularity exec <container> /usr/local/bin/bp_classify_hits_kingdom.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_classify_hits_kingdom.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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