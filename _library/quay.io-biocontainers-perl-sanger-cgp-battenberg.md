---
layout: container
name:  "quay.io/biocontainers/perl-sanger-cgp-battenberg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-sanger-cgp-battenberg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-sanger-cgp-battenberg/container.yaml"
updated_at: "2023-09-05 02:53:47.758718"
latest: "1.4.1--pl5321h031d066_9"
container_url: "https://biocontainers.pro/tools/perl-sanger-cgp-battenberg"
aliases:
 - "alleleCounter"
 - "alleleCounter.pl"
 - "bamToBw.pl"
 - "bam_stats.pl"
 - "bam_to_sra_sub.pl"
 - "battenberg.pl"
 - "battenberg_CN_to_VCF.pl"
 - "battenberg_version.pl"
 - "bwa_aln.pl"
 - "bwa_mem.pl"
 - "cgpAppendIdsToVcf.pl"
 - "cgpVCFSplit.pl"
 - "cover"
 - "cpancover"
 - "detectExtremeDepth.pl"
 - "diff_bams.pl"
 - "download_generate_bberg_ref_files.pl"
 - "gcov2perl"
 - "gnos_pull.pl"
 - "impute2"
 - "monitor.pl"
 - "ppi2html"
 - "tab-to-vcf"
 - "vcf-haplotypes"
 - "xam_coverage_bins.pl"
 - "xml_to_bas.pl"
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
 - "1.4.1--pl5321hec16e2b_8"
 - "1.4.1--pl5321h031d066_9"
description: "shpc-registry automated BioContainers addition for perl-sanger-cgp-battenberg"
config: {"url": "https://biocontainers.pro/tools/perl-sanger-cgp-battenberg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-sanger-cgp-battenberg", "latest": {"1.4.1--pl5321h031d066_9": "sha256:135141553dcfcb13b431bfee46f3282fe4922e08dfd83cd2aaf89ffb21d634b2"}, "tags": {"1.4.1--pl5321hec16e2b_8": "sha256:bff9d392d2121073c8882a304d3ab3719b5c90e85efab8f96b97534fd5592d5c", "1.4.1--pl5321h031d066_9": "sha256:135141553dcfcb13b431bfee46f3282fe4922e08dfd83cd2aaf89ffb21d634b2"}, "docker": "quay.io/biocontainers/perl-sanger-cgp-battenberg", "aliases": {"alleleCounter": "/usr/local/bin/alleleCounter", "alleleCounter.pl": "/usr/local/bin/alleleCounter.pl", "bamToBw.pl": "/usr/local/bin/bamToBw.pl", "bam_stats.pl": "/usr/local/bin/bam_stats.pl", "bam_to_sra_sub.pl": "/usr/local/bin/bam_to_sra_sub.pl", "battenberg.pl": "/usr/local/bin/battenberg.pl", "battenberg_CN_to_VCF.pl": "/usr/local/bin/battenberg_CN_to_VCF.pl", "battenberg_version.pl": "/usr/local/bin/battenberg_version.pl", "bwa_aln.pl": "/usr/local/bin/bwa_aln.pl", "bwa_mem.pl": "/usr/local/bin/bwa_mem.pl", "cgpAppendIdsToVcf.pl": "/usr/local/bin/cgpAppendIdsToVcf.pl", "cgpVCFSplit.pl": "/usr/local/bin/cgpVCFSplit.pl", "cover": "/usr/local/bin/cover", "cpancover": "/usr/local/bin/cpancover", "detectExtremeDepth.pl": "/usr/local/bin/detectExtremeDepth.pl", "diff_bams.pl": "/usr/local/bin/diff_bams.pl", "download_generate_bberg_ref_files.pl": "/usr/local/bin/download_generate_bberg_ref_files.pl", "gcov2perl": "/usr/local/bin/gcov2perl", "gnos_pull.pl": "/usr/local/bin/gnos_pull.pl", "impute2": "/usr/local/bin/impute2", "monitor.pl": "/usr/local/bin/monitor.pl", "ppi2html": "/usr/local/bin/ppi2html", "tab-to-vcf": "/usr/local/bin/tab-to-vcf", "vcf-haplotypes": "/usr/local/bin/vcf-haplotypes", "xam_coverage_bins.pl": "/usr/local/bin/xam_coverage_bins.pl", "xml_to_bas.pl": "/usr/local/bin/xml_to_bas.pl", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-sanger-cgp-battenberg.
shpc-registry automated BioContainers addition for perl-sanger-cgp-battenberg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-battenberg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-sanger-cgp-battenberg:1.4.1--pl5321h031d066_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-sanger-cgp-battenberg/1.4.1--pl5321h031d066_9
$ module help quay.io/biocontainers/perl-sanger-cgp-battenberg/1.4.1--pl5321h031d066_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-sanger-cgp-battenberg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-battenberg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-sanger-cgp-battenberg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-sanger-cgp-battenberg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-sanger-cgp-battenberg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-sanger-cgp-battenberg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alleleCounter

```bash
$ singularity exec <container> /usr/local/bin/alleleCounter
$ podman run --it --rm --entrypoint /usr/local/bin/alleleCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleCounter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alleleCounter.pl

```bash
$ singularity exec <container> /usr/local/bin/alleleCounter.pl
$ podman run --it --rm --entrypoint /usr/local/bin/alleleCounter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleCounter.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBw.pl

```bash
$ singularity exec <container> /usr/local/bin/bamToBw.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBw.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBw.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_stats.pl

```bash
$ singularity exec <container> /usr/local/bin/bam_stats.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bam_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_stats.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam_to_sra_sub.pl

```bash
$ singularity exec <container> /usr/local/bin/bam_to_sra_sub.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bam_to_sra_sub.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_to_sra_sub.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### battenberg.pl

```bash
$ singularity exec <container> /usr/local/bin/battenberg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/battenberg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/battenberg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### battenberg_CN_to_VCF.pl

```bash
$ singularity exec <container> /usr/local/bin/battenberg_CN_to_VCF.pl
$ podman run --it --rm --entrypoint /usr/local/bin/battenberg_CN_to_VCF.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/battenberg_CN_to_VCF.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### battenberg_version.pl

```bash
$ singularity exec <container> /usr/local/bin/battenberg_version.pl
$ podman run --it --rm --entrypoint /usr/local/bin/battenberg_version.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/battenberg_version.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa_aln.pl

```bash
$ singularity exec <container> /usr/local/bin/bwa_aln.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bwa_aln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa_aln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa_mem.pl

```bash
$ singularity exec <container> /usr/local/bin/bwa_mem.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bwa_mem.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa_mem.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpAppendIdsToVcf.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpAppendIdsToVcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpAppendIdsToVcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgpVCFSplit.pl

```bash
$ singularity exec <container> /usr/local/bin/cgpVCFSplit.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgpVCFSplit.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cover

```bash
$ singularity exec <container> /usr/local/bin/cover
$ podman run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpancover

```bash
$ singularity exec <container> /usr/local/bin/cpancover
$ podman run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpancover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### detectExtremeDepth.pl

```bash
$ singularity exec <container> /usr/local/bin/detectExtremeDepth.pl
$ podman run --it --rm --entrypoint /usr/local/bin/detectExtremeDepth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/detectExtremeDepth.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diff_bams.pl

```bash
$ singularity exec <container> /usr/local/bin/diff_bams.pl
$ podman run --it --rm --entrypoint /usr/local/bin/diff_bams.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diff_bams.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_generate_bberg_ref_files.pl

```bash
$ singularity exec <container> /usr/local/bin/download_generate_bberg_ref_files.pl
$ podman run --it --rm --entrypoint /usr/local/bin/download_generate_bberg_ref_files.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_generate_bberg_ref_files.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov2perl

```bash
$ singularity exec <container> /usr/local/bin/gcov2perl
$ podman run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov2perl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnos_pull.pl

```bash
$ singularity exec <container> /usr/local/bin/gnos_pull.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gnos_pull.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnos_pull.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impute2

```bash
$ singularity exec <container> /usr/local/bin/impute2
$ podman run --it --rm --entrypoint /usr/local/bin/impute2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impute2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monitor.pl

```bash
$ singularity exec <container> /usr/local/bin/monitor.pl
$ podman run --it --rm --entrypoint /usr/local/bin/monitor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monitor.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppi2html

```bash
$ singularity exec <container> /usr/local/bin/ppi2html
$ podman run --it --rm --entrypoint /usr/local/bin/ppi2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppi2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tab-to-vcf

```bash
$ singularity exec <container> /usr/local/bin/tab-to-vcf
$ podman run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tab-to-vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf-haplotypes

```bash
$ singularity exec <container> /usr/local/bin/vcf-haplotypes
$ podman run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf-haplotypes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xam_coverage_bins.pl

```bash
$ singularity exec <container> /usr/local/bin/xam_coverage_bins.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xam_coverage_bins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xam_coverage_bins.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_to_bas.pl

```bash
$ singularity exec <container> /usr/local/bin/xml_to_bas.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xml_to_bas.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_to_bas.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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