package br.jus.tse.eleitoral.eleitor.integracao.webservices.soap.impl;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;

import org.springframework.beans.factory.annotation.Autowired;

import br.jus.tse.corporativa.arqjeespring.infra.exceptions.WebServicesException;
import br.jus.tse.corporativa.arqjeespring.infra.utils.conversores.ConversorTipoObjeto;
import br.jus.tse.corporativa.arqjeespring.infra.utils.string.StringArqUtils;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.enums.SituacaoInscricaoEnum;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.managers.IEleitorManager;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.Eleitor;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoAgregacao;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTemporario;
import br.jus.tse.eleitoral.eleitor.dominio.negocio.models.ViewLocalVotacaoTransito;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.EleitorSituacaoDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.LocalVotacaoAgregacaoDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.LocalVotacaoDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.LocalVotacaoTemporarioDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.dto.LocalVotacaoTransitoDTO;
import br.jus.tse.eleitoral.eleitor.integracao.webservices.soap.IEleitorSOAPService;

@WebService(
	endpointInterface = "br.jus.tse.eleitoral.eleitor.integracao.webservices.soap.IEleitorSOAPService",
	targetNamespace = "http://tse.jus.br/eleitoral/eleitor",
	portName = "EleitorPort"
)
@SOAPBinding(style = Style.RPC)
public class EleitorSOAPServiceImpl implements IEleitorSOAPService {

	@Autowired
	private IEleitorManager iEleitorManager;
	
	@Autowired
	private ConversorTipoObjeto conversorTipoObjeto;
	
	
	@Override
	public EleitorDTO pesquisarEleitorPorInscricao(String pNumInscricao) throws WebServicesException {
		
		Eleitor eleitor = null;
		EleitorDTO eleitorDTO = null;
		
		try {
			
			eleitor = iEleitorManager.buscarEleitorPeloNumeroInscricao(pNumInscricao);
			
			eleitorDTO = conversorTipoObjeto.converter(eleitor, EleitorDTO.class);
			
		} catch (Exception e) {
			
			throw new WebServicesException(e);
			
		}
		
		return eleitorDTO;
	}
	

	@Override
	public LocalVotacaoDTO pesquisarLocalVotacaoPorInscricaoDataNascimentoNomeMae(String pNumInscricao, 
																				  String pDataNascimentoAsString, 
																				  String pNomeMae) 
		throws WebServicesException {
		
		Eleitor eleitor = null;
		LocalVotacaoDTO localVotacaoDTO = null;
		LocalVotacaoAgregacaoDTO localVotacaoAgregacaoDTO = null; 
		ViewLocalVotacaoAgregacao localVotacaoAgregacao = null;
		ViewLocalVotacaoTemporario localVotacaoTemporario = null;
		LocalVotacaoTemporarioDTO localVotacaoTemporarioDTO = null;
		List<LocalVotacaoTransitoDTO> lstLocalVotacaoTransitoDTO = null;
		List<ViewLocalVotacaoTransito> lstLocalVotacaoTransito = null;
		LocalVotacaoTransitoDTO localVotacaoTransitoDTO = null;
		DateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
		Date dataNascimentoDt;
		
		try {

			if (StringArqUtils.isEmptyString(pDataNascimentoAsString) || pDataNascimentoAsString.length() != 10) {
				
				throw new WebServicesException("A data no formato inválido [dd/mm/yyyy]");
				
			} else {

				dataNascimentoDt = sdf.parse(pDataNascimentoAsString);
			
				eleitor = iEleitorManager.buscarEleitorPeloNumeroInscricaoDataNascimentoNomeMae(pNumInscricao, 
																								dataNascimentoDt, 
																								pNomeMae);
			
				if (eleitor != null) {

					localVotacaoDTO = new LocalVotacaoDTO();
					
					localVotacaoDTO.setInscricao(eleitor.getNumInscricao());
					localVotacaoDTO.setNomEleitor(eleitor.getNomEleitor());
					localVotacaoDTO.setNumSecao(eleitor.getSecao().getNumero());
					localVotacaoDTO.setNumZona(eleitor.getSecao().getToZonaEleitoral().getNumero());
					localVotacaoDTO.setCodObjetoLocal(eleitor.getSecao().getToLocalVotacao().getId());
					localVotacaoDTO.setNomLocal(eleitor.getSecao().getToLocalVotacao().getNome());
					localVotacaoDTO.setDesEndereco(eleitor.getSecao().getToLocalVotacao().getEndereco());
					localVotacaoDTO.setNomBairro(eleitor.getSecao().getToLocalVotacao().getToBairro().getNome());
					localVotacaoDTO.setNomMunicipio(eleitor.getSecao().getToLocalVotacao().getToMunicipio().getNome());
					localVotacaoDTO.setSglUf(eleitor.getSecao().getToLocalVotacao().getToMunicipio().getToUf().getSigla());
				
					//recupera agregacao
					localVotacaoAgregacao = iEleitorManager.buscarLocalVotacaoAgregacaoEleitor(eleitor.getId());
				
					if (localVotacaoAgregacao != null) {
						localVotacaoAgregacaoDTO = new LocalVotacaoAgregacaoDTO();
						localVotacaoAgregacaoDTO.setNumZona(localVotacaoAgregacao.getNumZona());
						localVotacaoAgregacaoDTO.setNumSecao(localVotacaoAgregacao.getNumSecao());
						localVotacaoAgregacaoDTO.setCodObjetoLocal(localVotacaoAgregacao.getCodObjetoLocal());
						localVotacaoAgregacaoDTO.setNomLocal(localVotacaoAgregacao.getNomLocal());
						localVotacaoAgregacaoDTO.setDesEndereco(localVotacaoAgregacao.getDesEndereco());
						localVotacaoAgregacaoDTO.setNomBairro(localVotacaoAgregacao.getNomBairro());
						localVotacaoAgregacaoDTO.setNomLocalidade(localVotacaoAgregacao.getNomLocalidade());
						localVotacaoAgregacaoDTO.setSglUf(localVotacaoAgregacao.getSglUf());
	
						localVotacaoDTO.setLocalVotacaoAgregacao(localVotacaoAgregacaoDTO);
					}
				
					//recupera local temporario
					localVotacaoTemporario = iEleitorManager.buscarLocalVotacaoTemporarioEleitor(eleitor.getId());
					if (localVotacaoTemporario != null) {
						localVotacaoTemporarioDTO = new LocalVotacaoTemporarioDTO();
						localVotacaoTemporarioDTO.setNumZona(localVotacaoTemporario.getNumZona());
						localVotacaoTemporarioDTO.setNumSecao(localVotacaoTemporario.getNumSecao());
						localVotacaoTemporarioDTO.setCodObjetoLocal(localVotacaoTemporario.getCodObjetoLocal());
						localVotacaoTemporarioDTO.setNomLocal(localVotacaoTemporario.getNomLocal());
						localVotacaoTemporarioDTO.setDesEndereco(localVotacaoTemporario.getDesEndereco());
						localVotacaoTemporarioDTO.setNomBairro(localVotacaoTemporario.getNomBairro());
						localVotacaoTemporarioDTO.setNomLocalidade(localVotacaoTemporario.getNomLocalidade());
						localVotacaoTemporarioDTO.setSglUf(localVotacaoTemporario.getSglUf());
	
						localVotacaoDTO.setLocalVotacaoTemporario(localVotacaoTemporarioDTO);
					}

					//recupera voto em transito
					lstLocalVotacaoTransitoDTO = null;
					lstLocalVotacaoTransito = iEleitorManager.buscarLocalVotacaoTransitoEleitor(eleitor.getId());
					
					if (lstLocalVotacaoTransito != null) {
						lstLocalVotacaoTransitoDTO = new ArrayList<LocalVotacaoTransitoDTO>();
					}
					
					for (ViewLocalVotacaoTransito localVotacaoTransito : lstLocalVotacaoTransito) {
						localVotacaoTransitoDTO = new LocalVotacaoTransitoDTO();
						localVotacaoTransitoDTO.setNumZona(localVotacaoTransito.getNumZona());
						localVotacaoTransitoDTO.setNumSecao(localVotacaoTransito.getNumSecao());
						localVotacaoTransitoDTO.setDesEleicao(localVotacaoTransito.getDesEleicao());
						localVotacaoTransitoDTO.setNomLocal(localVotacaoTransito.getNomLocal());
						localVotacaoTransitoDTO.setDesEndereco(localVotacaoTransito.getDesEndereco());
						localVotacaoTransitoDTO.setNomBairro(localVotacaoTransito.getNomBairro());
						localVotacaoTransitoDTO.setNomLocalidade(localVotacaoTransito.getNomLocalidade());
						localVotacaoTransitoDTO.setSglUf(localVotacaoTransito.getSglUf());
						localVotacaoTransitoDTO.setIndSituacao(localVotacaoTransito.getIndSituacao());
						lstLocalVotacaoTransitoDTO.add(localVotacaoTransitoDTO);
					}

					localVotacaoDTO.setLocalVotacaoTransito(lstLocalVotacaoTransitoDTO);

					//eleitorDTO = conversorTipoObjeto.converter(eleitor, EleitorDTO.class);
					
					//BeanUtils.copyProperties(eleitor, eleitorDTO);
					
					// TODO Glayton - revisar
					/*eleitorDTO.setNumeroSecao(eleitor.getSecao().getNumero() + "");
					eleitorDTO.setNumeroZona(eleitor.getSecao().getZona().getNumero() + "");
					eleitorDTO.setBairro(eleitor.getSecao().getLocalVotacao().getBairro().getNome());
					eleitorDTO.setMunicipio(eleitor.getSecao().getLocalVotacao().getMunicipio().getNome());
					eleitorDTO.setUf(eleitor.getSecao().getLocalVotacao().getMunicipio().getToUf().getSigla());
					eleitorDTO.setNomeLocal(eleitor.getSecao().getLocalVotacao().getNome());
					eleitorDTO.setEnderecoLocal(eleitor.getSecao().getLocalVotacao().getEndereco());*/
				
				} else {
					
					throw new WebServicesException("Os dados informados (nome, data de nascimento e/ou filiação) não conferem com aqueles constantes no Cadastro Eleitoral");

				}
				
			}
			
		} catch (ParseException pe) {
			throw new WebServicesException("A data no formato inválido [dd/mm/yyyy]");
		} catch (Exception e) {
			throw new WebServicesException(e);
		}
		
		return localVotacaoDTO;
	}


	@Override
	public LocalVotacaoDTO pesquisarLocalVotacaoPorNomeDataNascimentoNomeMae(String pNomeEleitor, 
																			 Integer pDataNascimentoAsNumber, 
																			 String pNomeMae) 
		throws WebServicesException {
		
		Eleitor eleitor = null;
		LocalVotacaoDTO localVotacaoDTO = null;
		ViewLocalVotacaoAgregacao localVotacaoAgregacao = null;
		LocalVotacaoAgregacaoDTO localVotacaoAgregacaoDTO = null;
		ViewLocalVotacaoTemporario localVotacaoTemporario = null;
		LocalVotacaoTemporarioDTO localVotacaoTemporarioDTO = null;
		List<LocalVotacaoTransitoDTO> lstLocalVotacaoTransitoDTO = null;
		List<ViewLocalVotacaoTransito> lstLocalVotacaoTransito = null;
		LocalVotacaoTransitoDTO localVotacaoTransitoDTO = null;
		
		try {
			/*
			if (dataNascimento != null && dataNascimento.length() != 10) {
				throw new ServiceException("A data no formato inválido [dd/mm/yyyy]");
			}
			DateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
			Date dataNascimentoDt;
			dataNascimentoDt = sdf.parse(dataNascimento);
			*/
			
			eleitor = iEleitorManager.buscarEleitorPeloNomeDataNascimentoNomeMae(pNomeEleitor, 
																				 pDataNascimentoAsNumber, 
																				 pNomeMae);
			
			if (eleitor != null) {
				
				localVotacaoDTO = new LocalVotacaoDTO();

				localVotacaoDTO.setInscricao(eleitor.getNumInscricao());
				localVotacaoDTO.setNomEleitor(eleitor.getNomEleitor());
				localVotacaoDTO.setNumSecao(eleitor.getSecao().getNumero());
				localVotacaoDTO.setNumZona(eleitor.getSecao().getToZonaEleitoral().getNumero());
				localVotacaoDTO.setNomLocal(eleitor.getSecao().getToLocalVotacao().getNome());
				localVotacaoDTO.setDesEndereco(eleitor.getSecao().getToLocalVotacao().getEndereco());
				localVotacaoDTO.setNomBairro(eleitor.getSecao().getToLocalVotacao().getToBairro().getNome());
				localVotacaoDTO.setNomMunicipio(eleitor.getSecao().getToLocalVotacao().getToMunicipio().getNome());
				localVotacaoDTO.setSglUf(eleitor.getSecao().getToLocalVotacao().getToMunicipio().getToUf().getSigla());

				//recupera agregacao
				localVotacaoAgregacao = iEleitorManager.buscarLocalVotacaoAgregacaoEleitor(eleitor.getId());
				
				if (localVotacaoAgregacao != null) {
					localVotacaoAgregacaoDTO = new LocalVotacaoAgregacaoDTO();
					localVotacaoAgregacaoDTO.setNumZona(localVotacaoAgregacao.getNumZona());
					localVotacaoAgregacaoDTO.setNumSecao(localVotacaoAgregacao.getNumSecao());
					localVotacaoAgregacaoDTO.setCodObjetoLocal(localVotacaoAgregacao.getCodObjetoLocal());
					localVotacaoAgregacaoDTO.setNomLocal(localVotacaoAgregacao.getNomLocal());
					localVotacaoAgregacaoDTO.setDesEndereco(localVotacaoAgregacao.getDesEndereco());
					localVotacaoAgregacaoDTO.setNomBairro(localVotacaoAgregacao.getNomBairro());
					localVotacaoAgregacaoDTO.setNomLocalidade(localVotacaoAgregacao.getNomLocalidade());
					localVotacaoAgregacaoDTO.setSglUf(localVotacaoAgregacao.getSglUf());

					localVotacaoDTO.setLocalVotacaoAgregacao(localVotacaoAgregacaoDTO);
				}
				
				//recupera local temporario
				localVotacaoTemporario = iEleitorManager.buscarLocalVotacaoTemporarioEleitor(eleitor.getId());
				if (localVotacaoTemporario != null) {
					localVotacaoTemporarioDTO = new LocalVotacaoTemporarioDTO();
					localVotacaoTemporarioDTO.setNumZona(localVotacaoTemporario.getNumZona());
					localVotacaoTemporarioDTO.setNumSecao(localVotacaoTemporario.getNumSecao());
					localVotacaoTemporarioDTO.setCodObjetoLocal(localVotacaoTemporario.getCodObjetoLocal());
					localVotacaoTemporarioDTO.setNomLocal(localVotacaoTemporario.getNomLocal());
					localVotacaoTemporarioDTO.setDesEndereco(localVotacaoTemporario.getDesEndereco());
					localVotacaoTemporarioDTO.setNomBairro(localVotacaoTemporario.getNomBairro());
					localVotacaoTemporarioDTO.setNomLocalidade(localVotacaoTemporario.getNomLocalidade());
					localVotacaoTemporarioDTO.setSglUf(localVotacaoTemporario.getSglUf());

					localVotacaoDTO.setLocalVotacaoTemporario(localVotacaoTemporarioDTO);
				}

				//recupera voto em transito
				lstLocalVotacaoTransitoDTO = null;
				lstLocalVotacaoTransito = iEleitorManager.buscarLocalVotacaoTransitoEleitor(eleitor.getId());
				
				if (lstLocalVotacaoTransito != null) {
					lstLocalVotacaoTransitoDTO = new ArrayList<LocalVotacaoTransitoDTO>();
				}
				
				for (ViewLocalVotacaoTransito localVotacaoTransito : lstLocalVotacaoTransito) {
					localVotacaoTransitoDTO = new LocalVotacaoTransitoDTO();
					localVotacaoTransitoDTO.setNumZona(localVotacaoTransito.getNumZona());
					localVotacaoTransitoDTO.setNumSecao(localVotacaoTransito.getNumSecao());
					localVotacaoTransitoDTO.setDesEleicao(localVotacaoTransito.getDesEleicao());
					localVotacaoTransitoDTO.setNomLocal(localVotacaoTransito.getNomLocal());
					localVotacaoTransitoDTO.setDesEndereco(localVotacaoTransito.getDesEndereco());
					localVotacaoTransitoDTO.setNomBairro(localVotacaoTransito.getNomBairro());
					localVotacaoTransitoDTO.setNomLocalidade(localVotacaoTransito.getNomLocalidade());
					localVotacaoTransitoDTO.setSglUf(localVotacaoTransito.getSglUf());
					localVotacaoTransitoDTO.setIndSituacao(localVotacaoTransito.getIndSituacao());
					lstLocalVotacaoTransitoDTO.add(localVotacaoTransitoDTO);
				}
				localVotacaoDTO.setLocalVotacaoTransito(lstLocalVotacaoTransitoDTO);

				//eleitorDTO = conversorTipoObjeto.converter(eleitor, EleitorDTO.class);
				
				//BeanUtils.copyProperties(eleitor, eleitorDTO);
				
				// TODO Glayton - revisar
				/*eleitorDTO.setNumeroSecao(eleitor.getSecao().getNumero() + "");
				eleitorDTO.setNumeroZona(eleitor.getSecao().getZona().getNumero() + "");
				eleitorDTO.setBairro(eleitor.getSecao().getLocalVotacao().getBairro().getNome());
				eleitorDTO.setMunicipio(eleitor.getSecao().getLocalVotacao().getMunicipio().getNome());
				eleitorDTO.setUf(eleitor.getSecao().getLocalVotacao().getMunicipio().getToUf().getSigla());
				eleitorDTO.setNomeLocal(eleitor.getSecao().getLocalVotacao().getNome());
				eleitorDTO.setEnderecoLocal(eleitor.getSecao().getLocalVotacao().getEndereco());*/
			
			} else {
				
				throw new WebServicesException("Os dados informados (nome, data de nascimento e/ou filiação) não conferem com aqueles constantes no Cadastro Eleitoral");
				
			}
			
		} catch (Exception e) {
			throw new WebServicesException(e);
		}
		
		return localVotacaoDTO;
	}
	
	
	@Override
	public EleitorSituacaoDTO pesquisarSituacao(String inscricao) throws WebServicesException {
		
		Eleitor eleitor = null;
		EleitorSituacaoDTO eleitorSituacaoDTO = null;
		
		try {
			
			eleitor = iEleitorManager.buscarEleitorPeloNumeroInscricao(inscricao);
			
			if (eleitor != null) {
				
				eleitorSituacaoDTO = new EleitorSituacaoDTO();
				
				eleitorSituacaoDTO.setInscricao(inscricao);
				eleitorSituacaoDTO.setNome(eleitor.getNomEleitor());
				eleitorSituacaoDTO.setSituacao(SituacaoInscricaoEnum.valueOf(eleitor.getCodSitEleitor()));

			} else {
				
				throw new WebServicesException("Inscrição não encontrada no Cadastro Eleitoral.");
				
			}
			
		} catch (Exception e) {
			throw new WebServicesException(e);
		}
		
		return eleitorSituacaoDTO;
	}

}
