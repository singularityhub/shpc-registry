---
layout: container
name:  "quay.io/biocontainers/ice-cream"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ice-cream/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ice-cream/container.yaml"
updated_at: "2023-10-30 04:26:20.176647"
latest: "1.10--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/ice-cream"
aliases:
 - "ICEcream.sh"
 - "Vmatchtrans.pl"
 - "chain2dim"
 - "cleanpp.sh"
 - "jwebserver"
 - "matchcluster"
 - "mkdna6idx"
 - "mkvtree"
 - "plotting_script.py"
 - "repfind.pl"
 - "upgradeprj.pl"
 - "vendian"
 - "vmatch"
 - "vmatchselect"
 - "vmigrate.sh"
 - "vseqinfo"
 - "vseqselect"
 - "vstree2tex"
 - "vsubseqselect"
 - "blastn_vdb"
 - "tbl2asn-test"
 - "tblastn_vdb"
 - "TMalign"
 - "make_pscores.pl"
 - "poa"
 - "fix-sqn-date"
 - "faketime"
 - "real-tbl2asn"
 - "prokka-abricate_to_fasta_db"
 - "clustalo"
 - "prokka"
 - "prokka-biocyc_to_fasta_db"
 - "prokka-build_kingdom_dbs"
 - "prokka-cdd_to_hmm"
 - "prokka-clusters_to_hmm"
 - "prokka-genbank_to_fasta_db"
 - "prokka-genpept_to_fasta_db"
 - "prokka-hamap_to_hmm"
 - "prokka-tigrfams_to_hmm"
 - "prokka-uniprot_to_fasta_db"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
versions:
 - "1.10--hdfd78af_0"
 - "1.10--hdfd78af_1"
description: "singularity registry hpc automated addition for ice-cream"
config: {"url": "https://biocontainers.pro/tools/ice-cream", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ice-cream", "latest": {"1.10--hdfd78af_1": "sha256:877571755bf20e957a9cd08ef65204db783782cac91a7c1126f0d2f298a4342d"}, "tags": {"1.10--hdfd78af_0": "sha256:88074ba949163f7cb21ff9a51df4ec6257083c96f80cfedd02d4d63ecd246c09", "1.10--hdfd78af_1": "sha256:877571755bf20e957a9cd08ef65204db783782cac91a7c1126f0d2f298a4342d"}, "docker": "quay.io/biocontainers/ice-cream", "aliases": {"ICEcream.sh": "/usr/local/bin/ICEcream.sh", "Vmatchtrans.pl": "/usr/local/bin/Vmatchtrans.pl", "chain2dim": "/usr/local/bin/chain2dim", "cleanpp.sh": "/usr/local/bin/cleanpp.sh", "jwebserver": "/usr/local/bin/jwebserver", "matchcluster": "/usr/local/bin/matchcluster", "mkdna6idx": "/usr/local/bin/mkdna6idx", "mkvtree": "/usr/local/bin/mkvtree", "plotting_script.py": "/usr/local/bin/plotting_script.py", "repfind.pl": "/usr/local/bin/repfind.pl", "upgradeprj.pl": "/usr/local/bin/upgradeprj.pl", "vendian": "/usr/local/bin/vendian", "vmatch": "/usr/local/bin/vmatch", "vmatchselect": "/usr/local/bin/vmatchselect", "vmigrate.sh": "/usr/local/bin/vmigrate.sh", "vseqinfo": "/usr/local/bin/vseqinfo", "vseqselect": "/usr/local/bin/vseqselect", "vstree2tex": "/usr/local/bin/vstree2tex", "vsubseqselect": "/usr/local/bin/vsubseqselect", "blastn_vdb": "/usr/local/bin/blastn_vdb", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "TMalign": "/usr/local/bin/TMalign", "make_pscores.pl": "/usr/local/bin/make_pscores.pl", "poa": "/usr/local/bin/poa", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "faketime": "/usr/local/bin/faketime", "real-tbl2asn": "/usr/local/bin/real-tbl2asn", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "clustalo": "/usr/local/bin/clustalo", "prokka": "/usr/local/bin/prokka", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm", "prokka-genbank_to_fasta_db": "/usr/local/bin/prokka-genbank_to_fasta_db", "prokka-genpept_to_fasta_db": "/usr/local/bin/prokka-genpept_to_fasta_db", "prokka-hamap_to_hmm": "/usr/local/bin/prokka-hamap_to_hmm", "prokka-tigrfams_to_hmm": "/usr/local/bin/prokka-tigrfams_to_hmm", "prokka-uniprot_to_fasta_db": "/usr/local/bin/prokka-uniprot_to_fasta_db", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ice-cream.
singularity registry hpc automated addition for ice-cream
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ice-cream
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ice-cream:1.10--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ice-cream/1.10--hdfd78af_1
$ module help quay.io/biocontainers/ice-cream/1.10--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ice-cream-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ice-cream-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ice-cream-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ice-cream-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ice-cream-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ice-cream-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ICEcream.sh

```bash
$ singularity exec <container> /usr/local/bin/ICEcream.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ICEcream.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ICEcream.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Vmatchtrans.pl

```bash
$ singularity exec <container> /usr/local/bin/Vmatchtrans.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Vmatchtrans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Vmatchtrans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chain2dim

```bash
$ singularity exec <container> /usr/local/bin/chain2dim
$ podman run --it --rm --entrypoint /usr/local/bin/chain2dim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chain2dim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleanpp.sh

```bash
$ singularity exec <container> /usr/local/bin/cleanpp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cleanpp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanpp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jwebserver

```bash
$ singularity exec <container> /usr/local/bin/jwebserver
$ podman run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jwebserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matchcluster

```bash
$ singularity exec <container> /usr/local/bin/matchcluster
$ podman run --it --rm --entrypoint /usr/local/bin/matchcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matchcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkdna6idx

```bash
$ singularity exec <container> /usr/local/bin/mkdna6idx
$ podman run --it --rm --entrypoint /usr/local/bin/mkdna6idx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkdna6idx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkvtree

```bash
$ singularity exec <container> /usr/local/bin/mkvtree
$ podman run --it --rm --entrypoint /usr/local/bin/mkvtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkvtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotting_script.py

```bash
$ singularity exec <container> /usr/local/bin/plotting_script.py
$ podman run --it --rm --entrypoint /usr/local/bin/plotting_script.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotting_script.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repfind.pl

```bash
$ singularity exec <container> /usr/local/bin/repfind.pl
$ podman run --it --rm --entrypoint /usr/local/bin/repfind.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repfind.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upgradeprj.pl

```bash
$ singularity exec <container> /usr/local/bin/upgradeprj.pl
$ podman run --it --rm --entrypoint /usr/local/bin/upgradeprj.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upgradeprj.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vendian

```bash
$ singularity exec <container> /usr/local/bin/vendian
$ podman run --it --rm --entrypoint /usr/local/bin/vendian   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vendian   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmatch

```bash
$ singularity exec <container> /usr/local/bin/vmatch
$ podman run --it --rm --entrypoint /usr/local/bin/vmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmatchselect

```bash
$ singularity exec <container> /usr/local/bin/vmatchselect
$ podman run --it --rm --entrypoint /usr/local/bin/vmatchselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmatchselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmigrate.sh

```bash
$ singularity exec <container> /usr/local/bin/vmigrate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/vmigrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmigrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vseqinfo

```bash
$ singularity exec <container> /usr/local/bin/vseqinfo
$ podman run --it --rm --entrypoint /usr/local/bin/vseqinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vseqinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vseqselect

```bash
$ singularity exec <container> /usr/local/bin/vseqselect
$ podman run --it --rm --entrypoint /usr/local/bin/vseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vstree2tex

```bash
$ singularity exec <container> /usr/local/bin/vstree2tex
$ podman run --it --rm --entrypoint /usr/local/bin/vstree2tex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vstree2tex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsubseqselect

```bash
$ singularity exec <container> /usr/local/bin/vsubseqselect
$ podman run --it --rm --entrypoint /usr/local/bin/vsubseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsubseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pscores.pl

```bash
$ singularity exec <container> /usr/local/bin/make_pscores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix-sqn-date

```bash
$ singularity exec <container> /usr/local/bin/fix-sqn-date
$ podman run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faketime

```bash
$ singularity exec <container> /usr/local/bin/faketime
$ podman run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### real-tbl2asn

```bash
$ singularity exec <container> /usr/local/bin/real-tbl2asn
$ podman run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-abricate_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-abricate_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka

```bash
$ singularity exec <container> /usr/local/bin/prokka
$ podman run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-biocyc_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-biocyc_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-biocyc_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-biocyc_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-build_kingdom_dbs

```bash
$ singularity exec <container> /usr/local/bin/prokka-build_kingdom_dbs
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-build_kingdom_dbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-build_kingdom_dbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-cdd_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-cdd_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-cdd_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-cdd_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-clusters_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-clusters_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-clusters_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-clusters_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-genbank_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-genbank_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-genbank_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-genbank_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-genpept_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-genpept_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-genpept_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-genpept_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-hamap_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-hamap_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-hamap_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-hamap_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-tigrfams_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-tigrfams_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-tigrfams_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-tigrfams_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-uniprot_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-uniprot_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-uniprot_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-uniprot_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
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