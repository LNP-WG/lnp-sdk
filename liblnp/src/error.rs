// LNP C bindings library (liblnp)
// Written in 2020 by
//     Dr. Maxim Orlovsky <orlovsky@pandoracore.com>
//
// To the extent possible under law, the author(s) have dedicated all
// copyright and related and neighboring rights to this software to
// the public domain worldwide. This software is distributed without
// any warranty.
//
// You should have received a copy of the MIT License
// along with this software.
// If not, see <https://opensource.org/licenses/MIT>.

#[derive(Debug, Display, From, Error)]
#[display(doc_comments)]
#[non_exhaustive]
pub(crate) enum RequestError {
    /// Bech32 error: {_0}
    #[from]
    Bech32(lnpbp::rgb::bech32::Error),

    /// Input value is not a JSON object or JSON parse error: {_0}
    #[from]
    Json(serde_json::Error),

    // /// Invoice error: {_0}
    // #[from]
    // Invoice(lnp::fungible::InvoiceError),
    /// Input value is not a UTF8 string: {_0}
    #[from]
    Utf8(std::str::Utf8Error),

    /// Invalid network/chain identifier: {_0}
    #[from]
    ChainParse(lnpbp::bp::chain::ParseError),

    /// Bootstrap error: {_0}
    #[from]
    Runtime(lnp::Error),

    /// Transport error: {_0}
    #[from]
    Transport(lnpbp::lnp::transport::Error),

    // /// Integration error: {_0}
    // #[from]
    // Integration(lnp::i9n::Error),
    /// Impossible error: {_0}
    #[from]
    Infallible(std::convert::Infallible),

    /// Outpoint parsing error: {_0}
    #[from]
    Outpoint(lnpbp::bitcoin::blockdata::transaction::ParseOutPointError),

    /// I/O error: {_0}
    #[from]
    Io(std::io::Error),

    /// Input error: {_0}
    #[from]
    Input(String),

    /// Strict encoding error: {_0}
    #[from]
    StrictEncoding(lnpbp::strict_encoding::Error),
}
