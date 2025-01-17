let 
  nixpkgs = import <nixpkgs> {};
in
  with nixpkgs;
  stdenv.mkDerivation {
    name = "music-reader-env";
    buildInputs = [ 
      python312Packages.feedparser
      python312Packages.html2text
      ];
    OPENSSL_DEV=openssl.dev;
  }
