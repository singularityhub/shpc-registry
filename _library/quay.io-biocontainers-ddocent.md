---
layout: container
name:  "quay.io/biocontainers/ddocent"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ddocent/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ddocent/container.yaml"
updated_at: "2023-10-03 03:07:26.869318"
latest: "2.9.4--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/ddocent"
aliases:
 - "ErrorCount.sh"
 - "RefMapOpt.sh"
 - "ReferenceOpt.sh"
 - "Rename_SequenceFiles.sh"
 - "dDocent"
 - "dDocent_filters"
 - "filter_hwe_by_pop.pl"
 - "filter_missing_ind.sh"
 - "mawk"
 - "pear"
 - "pearRM"
 - "pop_missing_filter.sh"
 - "rainbow"
 - "remake_reference.sh"
 - "remove.bad.hap.loci.sh"
 - "sam_add_rg.pl"
 - "select_all_rbcontig.pl"
 - "select_all_rbcontig.pl.bak"
 - "select_best_rbcontig.pl"
 - "select_best_rbcontig.pl.bak"
 - "select_best_rbcontig_plus_read1.pl"
 - "select_best_rbcontig_plus_read1.pl.bak"
 - "select_sec_rbcontig.pl"
 - "select_sec_rbcontig.pl.bak"
 - "split_ref_by_bai_datasize.py"
 - "update_version.sh"
 - "vcftools"
 - "fill-aa"
 - "fill-an-ac"
 - "fill-fs"
 - "fill-ref-md5"
 - "vcf-annotate"
 - "vcf-compare"
 - "vcf-concat"
 - "vcf-consensus"
 - "vcf-contrast"
 - "vcf-convert"
versions:
 - "2.9.4--hdfd78af_0"
 - "2.9.4--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for ddocent"
config: {"url": "https://biocontainers.pro/tools/ddocent", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ddocent", "latest": {"2.9.4--hdfd78af_1": "sha256:64ef7f812b2756f211718eea882c039d109286874f8d029aab64bbf9619de8e8"}, "tags": {"2.9.4--hdfd78af_0": "sha256:ca1589c8586e16baff5f4751b5eb2ab033a710f89837422ffbcde66b58dd7225", "2.9.4--hdfd78af_1": "sha256:64ef7f812b2756f211718eea882c039d109286874f8d029aab64bbf9619de8e8"}, "docker": "quay.io/biocontainers/ddocent", "aliases": {"ErrorCount.sh": "/usr/local/bin/ErrorCount.sh", "RefMapOpt.sh": "/usr/local/bin/RefMapOpt.sh", "ReferenceOpt.sh": "/usr/local/bin/ReferenceOpt.sh", "Rename_SequenceFiles.sh": "/usr/local/bin/Rename_SequenceFiles.sh", "dDocent": "/usr/local/bin/dDocent", "dDocent_filters": "/usr/local/bin/dDocent_filters", "filter_hwe_by_pop.pl": "/usr/local/bin/filter_hwe_by_pop.pl", "filter_missing_ind.sh": "/usr/local/bin/filter_missing_ind.sh", "mawk": "/usr/local/bin/mawk", "pear": "/usr/local/bin/pear", "pearRM": "/usr/local/bin/pearRM", "pop_missing_filter.sh": "/usr/local/bin/pop_missing_filter.sh", "rainbow": "/usr/local/bin/rainbow", "remake_reference.sh": "/usr/local/bin/remake_reference.sh", "remove.bad.hap.loci.sh": "/usr/local/bin/remove.bad.hap.loci.sh", "sam_add_rg.pl": "/usr/local/bin/sam_add_rg.pl", "select_all_rbcontig.pl": "/usr/local/bin/select_all_rbcontig.pl", "select_all_rbcontig.pl.bak": "/usr/local/bin/select_all_rbcontig.pl.bak", "select_best_rbcontig.pl": "/usr/local/bin/select_best_rbcontig.pl", "select_best_rbcontig.pl.bak": "/usr/local/bin/select_best_rbcontig.pl.bak", "select_best_rbcontig_plus_read1.pl": "/usr/local/bin/select_best_rbcontig_plus_read1.pl", "select_best_rbcontig_plus_read1.pl.bak": "/usr/local/bin/select_best_rbcontig_plus_read1.pl.bak", "select_sec_rbcontig.pl": "/usr/local/bin/select_sec_rbcontig.pl", "select_sec_rbcontig.pl.bak": "/usr/local/bin/select_sec_rbcontig.pl.bak", "split_ref_by_bai_datasize.py": "/usr/local/bin/split_ref_by_bai_datasize.py", "update_version.sh": "/usr/local/bin/update_version.sh", "vcftools": "/usr/local/bin/vcftools", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ddocent.
shpc-registry automated BioContainers addition for ddocent
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ddocent
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ddocent:2.9.4--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ddocent/2.9.4--hdfd78af_1
$ module help quay.io/biocontainers/ddocent/2.9.4--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ddocent-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ddocent-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ddocent-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ddocent-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ddocent-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ddocent-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ErrorCount.sh

```bash
$ singularity exec <container> /usr/local/bin/ErrorCount.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ErrorCount.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ErrorCount.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RefMapOpt.sh

```bash
$ singularity exec <container> /usr/local/bin/RefMapOpt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/RefMapOpt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RefMapOpt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ReferenceOpt.sh

```bash
$ singularity exec <container> /usr/local/bin/ReferenceOpt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ReferenceOpt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ReferenceOpt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rename_SequenceFiles.sh

```bash
$ singularity exec <container> /usr/local/bin/Rename_SequenceFiles.sh
$ podman run --it --rm --entrypoint /usr/local/bin/Rename_SequenceFiles.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Rename_SequenceFiles.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dDocent

```bash
$ singularity exec <container> /usr/local/bin/dDocent
$ podman run --it --rm --entrypoint /usr/local/bin/dDocent   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dDocent   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dDocent_filters

```bash
$ singularity exec <container> /usr/local/bin/dDocent_filters
$ podman run --it --rm --entrypoint /usr/local/bin/dDocent_filters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dDocent_filters   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_hwe_by_pop.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_hwe_by_pop.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_hwe_by_pop.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_hwe_by_pop.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_missing_ind.sh

```bash
$ singularity exec <container> /usr/local/bin/filter_missing_ind.sh
$ podman run --it --rm --entrypoint /usr/local/bin/filter_missing_ind.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_missing_ind.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mawk

```bash
$ singularity exec <container> /usr/local/bin/mawk
$ podman run --it --rm --entrypoint /usr/local/bin/mawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pear

```bash
$ singularity exec <container> /usr/local/bin/pear
$ podman run --it --rm --entrypoint /usr/local/bin/pear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pearRM

```bash
$ singularity exec <container> /usr/local/bin/pearRM
$ podman run --it --rm --entrypoint /usr/local/bin/pearRM   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pearRM   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pop_missing_filter.sh

```bash
$ singularity exec <container> /usr/local/bin/pop_missing_filter.sh
$ podman run --it --rm --entrypoint /usr/local/bin/pop_missing_filter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pop_missing_filter.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rainbow

```bash
$ singularity exec <container> /usr/local/bin/rainbow
$ podman run --it --rm --entrypoint /usr/local/bin/rainbow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rainbow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remake_reference.sh

```bash
$ singularity exec <container> /usr/local/bin/remake_reference.sh
$ podman run --it --rm --entrypoint /usr/local/bin/remake_reference.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remake_reference.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove.bad.hap.loci.sh

```bash
$ singularity exec <container> /usr/local/bin/remove.bad.hap.loci.sh
$ podman run --it --rm --entrypoint /usr/local/bin/remove.bad.hap.loci.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove.bad.hap.loci.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam_add_rg.pl

```bash
$ singularity exec <container> /usr/local/bin/sam_add_rg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam_add_rg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_all_rbcontig.pl

```bash
$ singularity exec <container> /usr/local/bin/select_all_rbcontig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_all_rbcontig.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_all_rbcontig.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_all_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig.pl

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig_plus_read1.pl

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig_plus_read1.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_best_rbcontig_plus_read1.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_best_rbcontig_plus_read1.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_best_rbcontig_plus_read1.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_sec_rbcontig.pl

```bash
$ singularity exec <container> /usr/local/bin/select_sec_rbcontig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### select_sec_rbcontig.pl.bak

```bash
$ singularity exec <container> /usr/local/bin/select_sec_rbcontig.pl.bak
$ podman run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/select_sec_rbcontig.pl.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_ref_by_bai_datasize.py

```bash
$ singularity exec <container> /usr/local/bin/split_ref_by_bai_datasize.py
$ podman run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_ref_by_bai_datasize.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_version.sh

```bash
$ singularity exec <container> /usr/local/bin/update_version.sh
$ podman run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_version.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcftools

```bash
$ singularity exec <container> /usr/local/bin/vcftools
$ podman run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-aa

```bash
$ singularity exec <container> /usr/local/bin/fill-aa
$ podman run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-aa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-an-ac

```bash
$ singularity exec <container> /usr/local/bin/fill-an-ac
$ podman run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-an-ac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-fs

```bash
$ singularity exec <container> /usr/local/bin/fill-fs
$ podman run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fill-ref-md5

```bash
$ singularity exec <container> /usr/local/bin/fill-ref-md5
$ podman run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fill-ref-md5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-annotate

```bash
$ singularity exec <container> /usr/local/bin/vcf-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-compare

```bash
$ singularity exec <container> /usr/local/bin/vcf-compare
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-concat

```bash
$ singularity exec <container> /usr/local/bin/vcf-concat
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-consensus

```bash
$ singularity exec <container> /usr/local/bin/vcf-consensus
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-contrast

```bash
$ singularity exec <container> /usr/local/bin/vcf-contrast
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-contrast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-convert

```bash
$ singularity exec <container> /usr/local/bin/vcf-convert
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
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