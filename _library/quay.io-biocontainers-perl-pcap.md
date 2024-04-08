---
layout: container
name:  "quay.io/biocontainers/perl-pcap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-pcap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-pcap/container.yaml"
updated_at: "2024-04-08 02:33:45.419608"
latest: "3.5.2--pl5321hec16e2b_2"
container_url: "https://biocontainers.pro/tools/perl-pcap"
aliases:
 - "bamToBw.pl"
 - "bam_stats.pl"
 - "bam_to_sra_sub.pl"
 - "bwa_aln.pl"
 - "bwa_mem.pl"
 - "cgpAppendIdsToVcf.pl"
 - "cgpVCFSplit.pl"
 - "cover"
 - "cpancover"
 - "detectExtremeDepth.pl"
 - "diff_bams.pl"
 - "gcov2perl"
 - "gnos_pull.pl"
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
 - "3.5.2--pl5321hec16e2b_2"
description: "shpc-registry automated BioContainers addition for perl-pcap"
config: {"url": "https://biocontainers.pro/tools/perl-pcap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-pcap", "latest": {"3.5.2--pl5321hec16e2b_2": "sha256:bd2ae0beb471e456068db53ba6fa8cce228263ed43f44ddcbded8a71e46c046e"}, "tags": {"3.5.2--pl5321hec16e2b_2": "sha256:bd2ae0beb471e456068db53ba6fa8cce228263ed43f44ddcbded8a71e46c046e"}, "docker": "quay.io/biocontainers/perl-pcap", "aliases": {"bamToBw.pl": "/usr/local/bin/bamToBw.pl", "bam_stats.pl": "/usr/local/bin/bam_stats.pl", "bam_to_sra_sub.pl": "/usr/local/bin/bam_to_sra_sub.pl", "bwa_aln.pl": "/usr/local/bin/bwa_aln.pl", "bwa_mem.pl": "/usr/local/bin/bwa_mem.pl", "cgpAppendIdsToVcf.pl": "/usr/local/bin/cgpAppendIdsToVcf.pl", "cgpVCFSplit.pl": "/usr/local/bin/cgpVCFSplit.pl", "cover": "/usr/local/bin/cover", "cpancover": "/usr/local/bin/cpancover", "detectExtremeDepth.pl": "/usr/local/bin/detectExtremeDepth.pl", "diff_bams.pl": "/usr/local/bin/diff_bams.pl", "gcov2perl": "/usr/local/bin/gcov2perl", "gnos_pull.pl": "/usr/local/bin/gnos_pull.pl", "monitor.pl": "/usr/local/bin/monitor.pl", "ppi2html": "/usr/local/bin/ppi2html", "tab-to-vcf": "/usr/local/bin/tab-to-vcf", "vcf-haplotypes": "/usr/local/bin/vcf-haplotypes", "xam_coverage_bins.pl": "/usr/local/bin/xam_coverage_bins.pl", "xml_to_bas.pl": "/usr/local/bin/xml_to_bas.pl", "fill-aa": "/usr/local/bin/fill-aa", "fill-an-ac": "/usr/local/bin/fill-an-ac", "fill-fs": "/usr/local/bin/fill-fs", "fill-ref-md5": "/usr/local/bin/fill-ref-md5", "vcf-annotate": "/usr/local/bin/vcf-annotate", "vcf-compare": "/usr/local/bin/vcf-compare", "vcf-concat": "/usr/local/bin/vcf-concat", "vcf-consensus": "/usr/local/bin/vcf-consensus", "vcf-contrast": "/usr/local/bin/vcf-contrast", "vcf-convert": "/usr/local/bin/vcf-convert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-pcap.
shpc-registry automated BioContainers addition for perl-pcap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-pcap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-pcap:3.5.2--pl5321hec16e2b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-pcap/3.5.2--pl5321hec16e2b_2
$ module help quay.io/biocontainers/perl-pcap/3.5.2--pl5321hec16e2b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-pcap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-pcap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-pcap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-pcap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-pcap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-pcap-inspect-deffile:

```bash
$ singularity inspect -d <container>
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