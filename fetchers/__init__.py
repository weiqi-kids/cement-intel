"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .anhui_conch import AnhuiConchFetcher
from .asia_cement import AsiaCementFetcher
from .asia_cement_china import AsiaCementChinaFetcher
from .cemex import CemexFetcher
from .cnbm import CnbmFetcher
from .crh import CrhFetcher
from .eagle_materials import EagleMaterialsFetcher
from .heidelberg import HeidelbergFetcher
from .holcim import HolcimFetcher
from .martin_marietta import MartinMariettaFetcher
from .siam_cement import SiamCementFetcher
from .taiheiyo import TaiheiyoFetcher
from .taiwan_cement import TaiwanCementFetcher
from .thyssenkrupp import ThyssenkruppFetcher
from .ultratech import UltratechFetcher
from .vulcan import VulcanFetcher

FETCHERS = {
    "anhui_conch": AnhuiConchFetcher,
    "asia_cement": AsiaCementFetcher,
    "asia_cement_china": AsiaCementChinaFetcher,
    "cemex": CemexFetcher,
    "cnbm": CnbmFetcher,
    "crh": CrhFetcher,
    "eagle_materials": EagleMaterialsFetcher,
    "heidelberg": HeidelbergFetcher,
    "holcim": HolcimFetcher,
    "martin_marietta": MartinMariettaFetcher,
    "siam_cement": SiamCementFetcher,
    "taiheiyo": TaiheiyoFetcher,
    "taiwan_cement": TaiwanCementFetcher,
    "thyssenkrupp": ThyssenkruppFetcher,
    "ultratech": UltratechFetcher,
    "vulcan": VulcanFetcher,
}
