package br.jus.tse.eleitoral.eleitor.dominio.negocio.managers.impl;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import org.jboss.logging.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import br.jus.tse.corporativa.arqjeespring.infra.daos.IBaseCRUDDAO;
import br.jus.tse.corporativa.arqjeespring.infra.enums.EnumOperacoesCRUD;
import br.jus.tse.corporativa.arqjeespring.infra.exceptions.AplicacaoException;
import br.jus.tse.corporativa.arqjeespring.infra.utils.string.StringArqUtils;
import br.jus.tse.corporativa.arqjeespring.negocio.managers.impl.AbstractBaseCRUDManager;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IEleitorDAO;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IViewLocalVotacaoAgregacaoDAO;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IViewLocalVotacaoTemporarioDAO;
import br.jus.tse.eleitoral.eleitor.dominio.infra.daos.IViewLocalVotacaoTransitoDAO;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.exceptions.ParametroObrigatorioNaoInformadoException;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.managers.IEleitorManager;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.Eleitor;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoAgregacao;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTemporario;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTransito;

@Service
public class EleitorManager extends AbstractBaseCRUDManager<Eleitor, String> implements IEleitorManager {

	private static Logger logger = Logger.getLogger(EleitorManager.class);
	
	@Autowired
	private IEleitorDAO iEleitorDAO;

	@Autowired
	private IViewLocalVotacaoAgregacaoDAO iViewLocalVotacaoAgregacaoDAO;

	@Autowired
	private IViewLocalVotacaoTemporarioDAO iViewLocalVotacaoTemporarioDAO;

	@Autowired
	private IViewLocalVotacaoTransitoDAO iViewLocalVotacaoTransitoDAO;


	public EleitorManager() {
		
	}
	
	
	@Override
	protected IBaseCRUDDAO<Eleitor, String> getDAOResponsavel() {
		return iEleitorDAO;
	}

	
	
	@Override
	public Eleitor buscarEleitorPeloNumeroInscricao(String pNumInscricao) 
		throws AplicacaoException {
		
		Eleitor eleitor = null;

		try {
		
			if (!StringArqUtils.isEmptyString(pNumInscricao)) {

				eleitor = iEleitorDAO.findByNumeroInscricao(pNumInscricao);
				
				if (eleitor == null) {
					throw new ParametroObrigatorioNaoInformadoException("A inscrição informada não foi encontrada na base de dados");
				}

			} else {
				
				throw new ParametroObrigatorioNaoInformadoException("A inscrição é obrigatória");
				
			}
		
			
		} catch (Exception e) {
			throw new AplicacaoException(e);
		}
		
		return eleitor;
	}
	
	
	@Override
	public List<Eleitor> buscarEleitorPorDadosEspecialissimos(String pNumInscricao, 
															  Integer pDataNascimentoAsNumber, 
															  String pNomeEleitor, 
															  String pNomePai, 
															  String pNomeMae) 
		throws AplicacaoException {
		
		List<Eleitor> resultList = null;
		
		try {

			resultList = iEleitorDAO.findByDadosEspecialissimos(pNumInscricao, 
															  pDataNascimentoAsNumber, 
															  pNomeEleitor, 
															  pNomePai, 
															  pNomeMae);
		} catch (Exception e) {
			throw new AplicacaoException(e);
		}
		
		return resultList;
		
	}

	
	@Override
	public Eleitor buscarEleitorPeloNumeroInscricaoDataNascimentoNomeMae(String pNumInscricao, 
																		 Date pDataNascimento, 
																		 String pNomeMae) 
		throws AplicacaoException {

		Eleitor objResult = null;
		int iDataNascimento = -1;
		String nomeMaeLimpo = null;
		
		try {
		
			if (!StringArqUtils.isEmptyString(pNumInscricao)) {
	
				if (pDataNascimento != null) {
	
					if (!StringArqUtils.isEmptyString(pNomeMae)) {
	
						iDataNascimento = parseDate(pDataNascimento);
						nomeMaeLimpo = StringArqUtils.retirarAcentos(pNomeMae);
						
						objResult = iEleitorDAO.findByNumeroInscricaoDataNascimentoNomeMaeLimpo(pNumInscricao, 
																								iDataNascimento, 
																								nomeMaeLimpo);
					
					} else {
						
						throw new ParametroObrigatorioNaoInformadoException("O nome da mãe é obrigatório");
						
					}
			
				} else {
					
					throw new ParametroObrigatorioNaoInformadoException("A data de nascimento é obrigatória");
					
				}		
					
			} else {
						
				throw new ParametroObrigatorioNaoInformadoException("A inscrição é obrigatória");
	
			}
		
		} catch (Exception e) {
			throw new AplicacaoException(e);
		}
		
		return objResult;
		
	}

	
	
	@Override
	public Eleitor buscarEleitorPeloNomeDataNascimentoNomeMae(String pNomeEleitor, 
															  Integer pDataNascimentoAsNumber, 
															  String pNomeMae) 
		throws AplicacaoException {
		
		Eleitor objResult = null;
		String nomeEleitorLimpo = null;
		String nomeMaeLimpo = null;

		try {

			//int iDataNascimento = parseDate(dataNascimento);
			nomeEleitorLimpo = StringArqUtils.retirarAcentos(pNomeEleitor);
			nomeMaeLimpo = StringArqUtils.retirarAcentos(pNomeMae);
			
			objResult = iEleitorDAO.findByNomeDataNascimentoNomeMaeLimpo(nomeEleitorLimpo, 
																		 pDataNascimentoAsNumber, 
																		 nomeMaeLimpo);
	
		} catch (Exception e) {
			throw new AplicacaoException(e);
		}
		
		return objResult;
	}	
	
	
	@Override
	public ViewLocalVotacaoAgregacao buscarLocalVotacaoAgregacaoEleitor(String pCodObjEleitor) 
		throws AplicacaoException {
		
		ViewLocalVotacaoAgregacao localVotacaoAgregacao = null;

		try {
			
			localVotacaoAgregacao = iViewLocalVotacaoAgregacaoDAO.findByCodObjetoEleitor(pCodObjEleitor);

		} catch (Exception e) {
			throw new AplicacaoException(e);
		}
		
		return localVotacaoAgregacao;
	}
	

	@Override
	public ViewLocalVotacaoTemporario buscarLocalVotacaoTemporarioEleitor(String pCodObjEleitor) 
		throws AplicacaoException {
		
		ViewLocalVotacaoTemporario localVotacaoTemporario = null;
		
		try {

			localVotacaoTemporario = iViewLocalVotacaoTemporarioDAO.findByCodObjetoEleitor(pCodObjEleitor);
			
		} catch (Exception e) {
			throw new AplicacaoException(e);
		}

		return localVotacaoTemporario;
	}	
	

	@Override
	public List<ViewLocalVotacaoTransito> buscarLocalVotacaoTransitoEleitor(String pCodObjEleitor) 
		throws AplicacaoException {
		
		List<ViewLocalVotacaoTransito> lstLocalVotacaoTransito = null;

		try {
			
			lstLocalVotacaoTransito = iViewLocalVotacaoTransitoDAO.findByCodObjetoEleitor(pCodObjEleitor);
			
		} catch (Exception e) {
			throw new AplicacaoException(e);
		}

		return lstLocalVotacaoTransito;
	}


	private int parseDate(Date pDataAlvo) {
	    int intResult = 0;
        String strDataAlvo = null;
        
        strDataAlvo = formatDate(pDataAlvo, "yyyyMMdd");
        
        if (strDataAlvo != null) {
        	intResult = Integer.valueOf(strDataAlvo);
        }
        
        return intResult;
	}
	

	private String formatDate(Date pDataAlvo, String pFormato) {
		
	    String strResult = null;
	    SimpleDateFormat sdf = null;
	    
	    if (pDataAlvo != null && !StringArqUtils.isEmptyString(pFormato)) {
	        
	    	sdf = new SimpleDateFormat();
	        sdf.applyPattern( pFormato );
	        strResult = sdf.format( pDataAlvo );	        
	    }
	    
	    return strResult;
	}

	
	
	@Override
	public void validaRegras(Eleitor pEntidade, EnumOperacoesCRUD pOperacao) throws AplicacaoException {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void prepararEntidade(Eleitor pEntidade, EnumOperacoesCRUD pOperacao) throws AplicacaoException {
		// TODO Auto-generated method stub
		
	}	
	
	
}
